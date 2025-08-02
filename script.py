import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.ticker as ticker
import subprocess
import os
import numpy as np

# Load the dataset
df = pd.read_csv("freelancer_hourly_rates_2015_2025_monthly.csv")

# Setup the plot
fig, ax = plt.subplots(figsize=(12, 7))
plt.rcParams['font.family'] = 'DejaVu Sans'

# Get all unique years and create interpolated frames
years = sorted(df['Year'].unique())
interpolation_factor = 5  # Create 5 frames between each data point
smooth_years = []

for i in range(len(years) - 1):
    current_year = years[i]
    next_year = years[i + 1]
    
    for j in range(interpolation_factor):
        interpolated_year = current_year + (next_year - current_year) * j / interpolation_factor
        smooth_years.append(interpolated_year)

smooth_years.append(years[-1])  # Add the last year

# Function to interpolate data between two years
def interpolate_data(year1, year2, alpha):
    data1 = df[df['Year'] == year1].sort_values(by='HourlyRate', ascending=True).tail(10)
    data2 = df[df['Year'] == year2].sort_values(by='HourlyRate', ascending=True).tail(10)
    
    # Get all unique professions from both datasets
    all_professions = set(data1['Profession'].tolist() + data2['Profession'].tolist())
    
    interpolated_data = []
    for profession in all_professions:
        rate1 = data1[data1['Profession'] == profession]['HourlyRate'].values
        rate2 = data2[data2['Profession'] == profession]['HourlyRate'].values
        
        if len(rate1) > 0 and len(rate2) > 0:
            interpolated_rate = rate1[0] + (rate2[0] - rate1[0]) * alpha
        elif len(rate1) > 0:
            interpolated_rate = rate1[0]
        elif len(rate2) > 0:
            interpolated_rate = rate2[0]
        else:
            continue
            
        interpolated_data.append({'Profession': profession, 'HourlyRate': interpolated_rate})
    
    return pd.DataFrame(interpolated_data)

# Function to render each frame
def draw_frame(frame_idx):
    ax.clear()
    current_year = smooth_years[frame_idx]
    
    # Find the two nearest actual data points for interpolation
    if current_year in years:
        dff = df[df['Year'] == current_year].sort_values(by='HourlyRate', ascending=True).tail(10)
    else:
        # Find the two years to interpolate between
        for i in range(len(years) - 1):
            if years[i] <= current_year <= years[i + 1]:
                year1, year2 = years[i], years[i + 1]
                alpha = (current_year - year1) / (year2 - year1)
                dff = interpolate_data(year1, year2, alpha)
                dff = dff.sort_values(by='HourlyRate', ascending=True).tail(10)
                break
    
    if len(dff) > 0:
        bars = ax.barh(dff['Profession'], dff['HourlyRate'], color='#A3BFFA', alpha=0.8)
        
        # Add smooth animation effect to bars
        for i, bar in enumerate(bars):
            bar.set_width(dff.iloc[i]['HourlyRate'])
        
        dx = dff['HourlyRate'].max() / 200
        for i, (value, name) in enumerate(zip(dff['HourlyRate'], dff['Profession'])):
            ax.text(value - dx, i, f'${value:.2f}', size=12, weight='bold', ha='right', va='center', color='#1F2937')

    int_year = int(current_year)
    month_index = int(round((current_year - int_year) * 12))
    month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    if month_index < 12:
        month_label = f'{month_names[month_index]} {int_year}'
    else:
        month_label = f'Dec {int_year}'
    
    ax.text(1, 0.4, month_label, transform=ax.transAxes, size=40, ha='right', weight='bold', color='#111827')
    ax.set_title('Freelancer Hourly Rates by Profession (USD)', fontsize=22, pad=20, color='#111827', weight='bold')
    ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('${x:,.0f}'))
    ax.xaxis.set_ticks_position('none')
    ax.tick_params(axis='x', colors='#6B7280', labelsize=12)
    ax.set_xlim(0, df['HourlyRate'].max() + 10)
    ax.grid(which='major', axis='x', linestyle='--', color='#E5E7EB')
    
    # Add subtle currency indicator in top-right corner
    ax.text(0.98, 0.95, 'USD', transform=ax.transAxes, size=12, ha='right', va='top', 
            weight='normal', color='#9CA3AF', alpha=0.6)
    
    if len(dff) > 0:
        ax.set_yticks(range(len(dff)))
        ax.set_yticklabels(dff['Profession'], fontsize=14, color='#374151', ha='right')
    
    for spine in ['top', 'right', 'left', 'bottom']:
        ax.spines[spine].set_visible(False)

# Create animation with smoother frames
anim = animation.FuncAnimation(fig, draw_frame, frames=len(smooth_years), interval=100, repeat=False)

# Save as HD MP4 with higher frame rate
anim.save("freelancer_hourly_rates_2015_2025_temp.mp4", fps=24, dpi=200, extra_args=['-vcodec', 'libx264'])

# Add background music using ffmpeg
try:
    cmd = [
        'ffmpeg', '-y',
        '-i', 'freelancer_hourly_rates_2015_2025_temp.mp4',
        '-i', 'music/m1.mp3',
        '-c:v', 'copy',
        '-c:a', 'aac',
        '-shortest',
        'freelancer_hourly_rates_2015_2025.mp4'
    ]
    subprocess.run(cmd, check=True)
    
    # Clean up temporary file
    os.remove('freelancer_hourly_rates_2015_2025_temp.mp4')
    print("🎥 Video with background music saved as 'freelancer_hourly_rates_2015_2025.mp4'")
    
except subprocess.CalledProcessError:
    print("⚠️  ffmpeg not found or error occurred. Saving video without audio.")
    os.rename('freelancer_hourly_rates_2015_2025_temp.mp4', 'freelancer_hourly_rates_2015_2025.mp4')
    print("🎥 Video saved as 'freelancer_hourly_rates_2015_2025.mp4'")
except FileNotFoundError:
    print("⚠️  ffmpeg not found. Saving video without audio.")
    os.rename('freelancer_hourly_rates_2015_2025_temp.mp4', 'freelancer_hourly_rates_2015_2025.mp4')
    print("🎥 Video saved as 'freelancer_hourly_rates_2015_2025.mp4'")
