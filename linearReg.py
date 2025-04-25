import pandas as pd
import numpy as np

def estimate_coef(x, y):
    n = np.size(x)
    m_x, m_y = np.mean(x), np.mean(y)
    SS_xy = np.sum(y * x) - n * m_y * m_x
    SS_xx = np.sum(x * x) - n * m_x * m_x
    b_1 = SS_xy / SS_xx if SS_xx != 0 else np.nan
    b_0 = m_y - b_1 * m_x
    return b_0, b_1

def compute_r_squared(x, y, b_0, b_1):
    y_pred = b_0 + b_1 * x
    ss_total = np.sum((y - np.mean(y)) ** 2)
    ss_res = np.sum((y - y_pred) ** 2)
    r_squared = 1 - (ss_res / ss_total) if ss_total != 0 else np.nan
    return r_squared

def runLinearRegByANSI(file_path, output_path):
    df = pd.read_csv(file_path) 
    # df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
    # df['Crop_Yield'] = pd.to_numeric(df['Crop_Yield'], errors='coerce')
    # df['Anomaly'] = pd.to_numeric(df['Anomaly'], errors='coerce')
    df.dropna(subset=['Year', 'Crop_Yield', 'Anomaly', 'County_ANSI'], inplace=True)
    df = df.sort_values(by='Year')
    results = []

    # Group by ANSI
    for ansi, group in df.groupby('County_ANSI'):
        start_year = int(group['Year'].min())
        end_year = int(group['Year'].max())

        for start in range(start_year, end_year + 1, 5):
            end = start + 4
            period = group[(group['Year'] >= start) & (group['Year'] <= end)]

            if len(period) < 2:
                continue

            x = period['Anomaly'].to_numpy()
            y = period['Crop_Yield'].to_numpy()

            b_0, b_1 = estimate_coef(x, y)
            r2 = compute_r_squared(x, y, b_0, b_1)
            r = np.corrcoef(x, y)[0, 1] if len(x) > 1 else np.nan

            results.append({
                'ANSI': ansi,
                'Period': f"{start}-{end}",
                'Start Year': start,
                'End Year': end,
                'Intercept (b0)': round(b_0, 4),
                'Slope (b1)': round(b_1, 4),
                'R²': round(r2, 4),
                'Pearson r': round(r, 4),
                'Data Points': len(period)
})


    results_df = pd.DataFrame(results)
    results_df.to_csv(output_path, index=False)
    print(f"Results saved to: {output_path}")



