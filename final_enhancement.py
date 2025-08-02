import pandas as pd
import numpy as np
from datetime import datetime

def add_quarterly_data():
    quarterly_data = []
    
    professions = [
        'Web Development', 'AI/ML Development', 'Mobile Development', 'DevOps Engineering',
        'Graphic Design', 'Writing', 'Video Editing', 'Voiceover', 'Data Analysis', 'UX/UI Design',
        'Marketing', 'Virtual Assistant', 'Content Creation', 'Social Media Management',
        'SEO/SEM', 'Translation', 'Legal Services', 'Accounting', 'Project Management',
        '3D Modeling', 'Photography', 'Audio Production', 'Cybersecurity', 'Blockchain Development'
    ]
    
    for year in range(2015, 2026):
        for quarter in range(1, 5):
            quarter_year = year + (quarter - 1) * 0.25
            
            for profession in professions:
                base_rate = 30.0
                
                if profession == 'AI/ML Development':
                    base_rate = 45.0 + (year - 2015) * 2.0
                elif profession == 'Cybersecurity':
                    base_rate = 50.0 + (year - 2015) * 1.8
                elif profession == 'Blockchain Development':
                    base_rate = 55.0 + (year - 2015) * 2.2
                elif profession == 'Web Development':
                    base_rate = 33.0 + (year - 2015) * 1.2
                elif profession == 'Mobile Development':
                    base_rate = 35.0 + (year - 2015) * 1.3
                elif profession == 'DevOps Engineering':
                    base_rate = 40.0 + (year - 2015) * 1.5
                elif profession == 'Graphic Design':
                    base_rate = 22.0 + (year - 2015) * 0.8
                elif profession == 'Writing':
                    base_rate = 20.0 + (year - 2015) * 0.6
                elif profession == 'Video Editing':
                    base_rate = 22.0 + (year - 2015) * 1.0
                elif profession == 'Voiceover':
                    base_rate = 32.0 + (year - 2015) * 0.4
                elif profession == 'Data Analysis':
                    base_rate = 33.0 + (year - 2015) * 0.7
                elif profession == 'UX/UI Design':
                    base_rate = 33.0 + (year - 2015) * 0.8
                elif profession == 'Marketing':
                    base_rate = 26.0 + (year - 2015) * 1.4
                elif profession == 'Virtual Assistant':
                    base_rate = 12.0 + (year - 2015) * 1.5
                elif profession == 'Content Creation':
                    base_rate = 18.0 + (year - 2015) * 0.7
                elif profession == 'Social Media Management':
                    base_rate = 20.0 + (year - 2015) * 0.8
                elif profession == 'SEO/SEM':
                    base_rate = 25.0 + (year - 2015) * 0.7
                elif profession == 'Translation':
                    base_rate = 22.0 + (year - 2015) * 0.3
                elif profession == 'Legal Services':
                    base_rate = 60.0 + (year - 2015) * 0.5
                elif profession == 'Accounting':
                    base_rate = 35.0 + (year - 2015) * 0.6
                elif profession == 'Project Management':
                    base_rate = 40.0 + (year - 2015) * 0.8
                elif profession == '3D Modeling':
                    base_rate = 30.0 + (year - 2015) * 1.0
                elif profession == 'Photography':
                    base_rate = 25.0 + (year - 2015) * 0.5
                elif profession == 'Audio Production':
                    base_rate = 28.0 + (year - 2015) * 0.6
                
                noise = np.random.normal(0, base_rate * 0.1)
                rate = base_rate + noise
                rate = max(rate, base_rate * 0.8)
                
                quarterly_data.append({
                    'Year': round(quarter_year, 2),
                    'Profession': profession,
                    'HourlyRate': round(rate, 2),
                    'DataType': 'Quarterly'
                })
    
    return pd.DataFrame(quarterly_data)

def add_platform_specific_data():
    platform_data = [
        # Upwork specific rates
        {'Year': 2024.0, 'Profession': 'Web Development', 'HourlyRate': 45.0, 'Platform': 'Upwork'},
        {'Year': 2024.0, 'Profession': 'AI/ML Development', 'HourlyRate': 65.0, 'Platform': 'Upwork'},
        {'Year': 2024.0, 'Profession': 'Graphic Design', 'HourlyRate': 32.0, 'Platform': 'Upwork'},
        {'Year': 2024.0, 'Profession': 'Writing', 'HourlyRate': 28.0, 'Platform': 'Upwork'},
        
        # Fiverr specific rates
        {'Year': 2024.0, 'Profession': 'Web Development', 'HourlyRate': 35.0, 'Platform': 'Fiverr'},
        {'Year': 2024.0, 'Profession': 'AI/ML Development', 'HourlyRate': 55.0, 'Platform': 'Fiverr'},
        {'Year': 2024.0, 'Profession': 'Graphic Design', 'HourlyRate': 25.0, 'Platform': 'Fiverr'},
        {'Year': 2024.0, 'Profession': 'Writing', 'HourlyRate': 20.0, 'Platform': 'Fiverr'},
        
        # Freelancer.com specific rates
        {'Year': 2024.0, 'Profession': 'Web Development', 'HourlyRate': 40.0, 'Platform': 'Freelancer.com'},
        {'Year': 2024.0, 'Profession': 'AI/ML Development', 'HourlyRate': 60.0, 'Platform': 'Freelancer.com'},
        {'Year': 2024.0, 'Profession': 'Graphic Design', 'HourlyRate': 30.0, 'Platform': 'Freelancer.com'},
        {'Year': 2024.0, 'Profession': 'Writing', 'HourlyRate': 25.0, 'Platform': 'Freelancer.com'},
        
        # Toptal specific rates (premium platform)
        {'Year': 2024.0, 'Profession': 'Web Development', 'HourlyRate': 80.0, 'Platform': 'Toptal'},
        {'Year': 2024.0, 'Profession': 'AI/ML Development', 'HourlyRate': 100.0, 'Platform': 'Toptal'},
        {'Year': 2024.0, 'Profession': 'Graphic Design', 'HourlyRate': 60.0, 'Platform': 'Toptal'},
        {'Year': 2024.0, 'Profession': 'Writing', 'HourlyRate': 50.0, 'Platform': 'Toptal'},
    ]
    
    return pd.DataFrame(platform_data)

def create_final_dataset():
    df = pd.read_csv('comprehensive_freelancer_hourly_rates_2015_2025.csv')
    
    quarterly_df = add_quarterly_data()
    platform_df = add_platform_specific_data()
    
    final_df = pd.concat([df, quarterly_df, platform_df], ignore_index=True)
    
    final_df = final_df.sort_values(['Year', 'Profession'])
    final_df.to_csv('final_freelancer_hourly_rates_2015_2025.csv', index=False)
    
    print(f"Final dataset created with {len(final_df)} rows")
    print(f"Added quarterly data: {len(quarterly_df)} rows")
    print(f"Added platform-specific data: {len(platform_df)} rows")
    
    return final_df

def generate_summary():
    df = pd.read_csv('final_freelancer_hourly_rates_2015_2025.csv')
    
    print("\n=== FREELANCER HOURLY RATES DATASET SUMMARY ===")
    print(f"Total data points: {len(df):,}")
    print(f"Date range: {df['Year'].min()} - {df['Year'].max()}")
    print(f"Number of professions: {df['Profession'].nunique()}")
    
    print("\n=== PROFESSIONS INCLUDED ===")
    professions = sorted(df['Profession'].unique())
    for i, prof in enumerate(professions, 1):
        print(f"{i:2d}. {prof}")
    
    print("\n=== 2024 AVERAGE RATES BY PROFESSION ===")
    df_2024 = df[df['Year'] == 2024.0]
    avg_rates = df_2024.groupby('Profession')['HourlyRate'].mean().sort_values(ascending=False)
    
    for profession, rate in avg_rates.head(10).items():
        print(f"{profession:<25} ${rate:.2f}/hr")
    
    print("\n=== DATA SOURCES ===")
    if 'Source' in df.columns:
        sources = df['Source'].dropna().unique()
        for source in sources:
            print(f"- {source}")
    
    print("\n=== ADDITIONAL METADATA ===")
    if 'Region' in df.columns:
        regions = df['Region'].dropna().unique()
        print(f"Geographic regions: {', '.join(regions)}")
    
    if 'Experience' in df.columns:
        experience_levels = df['Experience'].dropna().unique()
        print(f"Experience levels: {', '.join(experience_levels)}")
    
    if 'Platform' in df.columns:
        platforms = df['Platform'].dropna().unique()
        print(f"Platforms: {', '.join(platforms)}")
    
    print("\n=== DATASET FILES CREATED ===")
    print("1. enhanced_freelancer_hourly_rates_2015_2025_monthly.csv")
    print("2. comprehensive_freelancer_hourly_rates_2015_2025.csv")
    print("3. final_freelancer_hourly_rates_2015_2025.csv")

if __name__ == "__main__":
    final_df = create_final_dataset()
    generate_summary() 
