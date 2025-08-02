import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_additional_professions():
    additional_professions = {
        'Mobile Development': {
            'base_rate_2015': 35.0,
            'growth_rate': 0.08,
            'volatility': 0.15
        },
        'AI/ML Development': {
            'base_rate_2015': 45.0,
            'growth_rate': 0.12,
            'volatility': 0.20
        },
        'DevOps Engineering': {
            'base_rate_2015': 40.0,
            'growth_rate': 0.10,
            'volatility': 0.18
        },
        'Content Creation': {
            'base_rate_2015': 18.0,
            'growth_rate': 0.06,
            'volatility': 0.12
        },
        'Social Media Management': {
            'base_rate_2015': 20.0,
            'growth_rate': 0.07,
            'volatility': 0.14
        },
        'SEO/SEM': {
            'base_rate_2015': 25.0,
            'growth_rate': 0.08,
            'volatility': 0.16
        },
        'Translation': {
            'base_rate_2015': 22.0,
            'growth_rate': 0.05,
            'volatility': 0.10
        },
        'Legal Services': {
            'base_rate_2015': 60.0,
            'growth_rate': 0.04,
            'volatility': 0.08
        },
        'Accounting': {
            'base_rate_2015': 35.0,
            'growth_rate': 0.05,
            'volatility': 0.12
        },
        'Project Management': {
            'base_rate_2015': 40.0,
            'growth_rate': 0.07,
            'volatility': 0.15
        },
        '3D Modeling': {
            'base_rate_2015': 30.0,
            'growth_rate': 0.09,
            'volatility': 0.17
        },
        'Photography': {
            'base_rate_2015': 25.0,
            'growth_rate': 0.06,
            'volatility': 0.13
        },
        'Audio Production': {
            'base_rate_2015': 28.0,
            'growth_rate': 0.07,
            'volatility': 0.14
        },
        'Cybersecurity': {
            'base_rate_2015': 50.0,
            'growth_rate': 0.11,
            'volatility': 0.19
        },
        'Blockchain Development': {
            'base_rate_2015': 55.0,
            'growth_rate': 0.13,
            'volatility': 0.25
        }
    }
    return additional_professions

def generate_monthly_data(profession, config, start_year=2015, end_year=2025):
    data = []
    current_rate = config['base_rate_2015']
    
    for year in np.arange(start_year, end_year + 0.1, 0.0833):
        for month in range(12):
            monthly_year = year + (month / 12.0)
            
            if monthly_year <= end_year:
                noise = np.random.normal(0, config['volatility'] * current_rate * 0.1)
                rate = current_rate + noise
                rate = max(rate, current_rate * 0.8)
                
                data.append({
                    'Year': round(monthly_year, 2),
                    'Profession': profession,
                    'HourlyRate': round(rate, 2)
                })
        
        current_rate *= (1 + config['growth_rate'] / 12)
    
    return data

def enhance_dataset():
    df = pd.read_csv('freelancer_hourly_rates_2015_2025_monthly.csv')
    
    additional_professions = generate_additional_professions()
    new_data = []
    
    for profession, config in additional_professions.items():
        profession_data = generate_monthly_data(profession, config)
        new_data.extend(profession_data)
    
    new_df = pd.DataFrame(new_data)
    enhanced_df = pd.concat([df, new_df], ignore_index=True)
    
    enhanced_df = enhanced_df.sort_values(['Year', 'Profession'])
    enhanced_df.to_csv('enhanced_freelancer_hourly_rates_2015_2025_monthly.csv', index=False)
    
    print(f"Original dataset: {len(df)} rows")
    print(f"Enhanced dataset: {len(enhanced_df)} rows")
    print(f"Added {len(new_df)} new data points")
    print(f"New professions added: {list(additional_professions.keys())}")
    
    return enhanced_df

if __name__ == "__main__":
    enhanced_df = enhance_dataset() 
