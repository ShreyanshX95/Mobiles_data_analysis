import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import streamlit as st
from io import BytesIO
import matplotlib.cm as cm
import matplotlib.colors as mcolors
from PIL import Image
import os
import base64


# ----- PAGE CONFIG -----
st.set_page_config(
    page_title="Mobile Phones Dataset",
    page_icon="📱",
    layout="wide",
)

# ----- LOAD INTER FONT & CUSTOM CSS -----
st.markdown(
    """
    <style>
        h1, h2, h3, h4, h5, h6 {
            color: white !important;
        }
        .stMarkdown p {
            color: white;
        }
    </style>
    <style>
    /* Use Inter font globally */
    html, body, [class*="css"]  {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen,
        Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif !important;
        background-color: #fff;
        color: #111;
        margin: 0;
        padding: 0;
    }

    

    /* Titles styling */
    h1, h2, h3 {
        font-weight: 600 !important;
        margin-bottom: 10px;
        margin-top: 0;
        color: #111;
    }

    /* Blue style for select, multiselect, buttons */
    div[data-baseweb="select"] > div > div {
        border-color: #0071e3 !important;
        color: #0071e3 !important;
        font-weight: 600;
    }
    div[data-baseweb="select"]:hover > div > div {
        border-color: #005bb5 !important;
    }

    /* Blue sidebar slider handle and track */
    .css-1cpxqw2 .stSlider .rc-slider-handle {
        background-color: #0071e3 !important;
        border-color: #0071e3 !important;
    }
    .css-1cpxqw2 .stSlider .rc-slider-track {
        background-color: #0071e3 !important;
    }

    /* Download button blue style */
    div.stDownloadButton > button {
        background-color: #0071e3 !important;
        color: white !important;
        font-weight: 600 !important;
        border-radius: 8px !important;
        padding: 8px 20px !important;
        transition: background-color 0.3s ease;
        cursor: pointer;
    }
    div.stDownloadButton > button:hover {
        background-color: #005bb5 !important;
        color: white !important;
    }

    /* Curved cards */
    .card {
        position: relative;
        border-radius: 20px;
        height: 180px;
        overflow: hidden;
        color: white;
        font-weight: 600;
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
        padding: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.15);
        background-size: cover !important;
        background-position: center !important;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .card:hover {
        transform: translateY(-10px);
        box-shadow: 0 18px 35px rgba(0,0,0,0.25);
    }

    /* Card title */
    .card-title {
        font-size: 1.5rem;
        margin-bottom: 6px;
        text-shadow: 1px 1px 5px rgba(0,0,0,0.7);
    }
    /* Card subtitle */
    .card-subtitle {
        font-size: 1.2rem;
        text-shadow: 1px 1px 5px rgba(0,0,0,0.7);
    }

    /* Hide Streamlit footer & native header */
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)



# ----- HEADER TITLE -----
st.markdown("<h1 style='color:#111; font-weight: 700;'>📱 Mobile Phones Dataset Analysis</h1>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# ----- LOAD DATAFRAME -----
data = {
    "company_name": ["Apple", "Samsung", "OnePlus", "Xiaomi", "Google"],
    "model_name": ["iPhone 16", "Galaxy S24", "OnePlus 12", "Redmi Note 13", "Pixel 8"],
    "mobile_weight_g": [174, 196, 203, 190, 187],
    "ram_gb": [6, 8, 12, 6, 8],
    "front_camera_mp": [12, 12, 16, 13, 10],
    "back_camera_mp": [48, 108, 50, 64, 50],
    "processor": ["A17 Bionic", "Snapdragon 8 Gen 2", "Snapdragon 8 Gen 3", "MediaTek 9200", "Tensor G3"],
    "battery_capacity_mah": [3600, 4000, 5000, 5020, 4355],
    "screen_size_inches": [6.1, 6.6, 6.7, 6.5, 6.2],
    "launched_price_pakistan_pkr": [224999, 194999, 169999, 89999, 144999],
    "launched_price_india_inr": [79999, 69999, 64999, 19999, 59999],
    "launched_price_china_cny": [5799, 4899, 4499, 1999, 4199],
    "launched_price_usa_usd": [799, 749, 699, 299, 699],
    "launched_price_dubai_aed": [2799, 2699, 2399, 999, 2499],
    "launched_year": [2024] * 5,
    "benchmark_score": [134000, 125000, 132000, 101000, 118000],
    "popular_country": ["USA", "South Korea", "India", "China", "Germany"],
    "popularity_%": [95, 88, 90, 85, 87],
    "storage_gb": [128.0, 256.0, 256.0, 128.0, 128.0]
    
}

mobiles = pd.DataFrame(data)

# Clean numeric columns for filtering
mobiles['battery_capacity_mah'] = pd.to_numeric(mobiles['battery_capacity_mah'], errors='coerce')
mobiles['storage_gb'] = pd.to_numeric(mobiles['storage_gb'], errors='coerce')
mobiles['screen_size_inches'] = pd.to_numeric(mobiles['screen_size_inches'], errors='coerce')
mobiles['ram_gb'] = pd.to_numeric(mobiles['ram_gb'], errors='coerce')
mobiles['launched_price_usa_usd'] = pd.to_numeric(mobiles['launched_price_usa_usd'], errors='coerce')
mobiles['benchmark_score'] = pd.to_numeric(mobiles['benchmark_score'], errors='coerce')
mobiles['popularity_%'] = pd.to_numeric(mobiles['popularity_%'], errors='coerce')

# Show dataframe
st.dataframe(mobiles, use_container_width=True)

# ----- DOWNLOAD BUTTONS -----
col1, col2 = st.columns(2)
with col1:
    csv = mobiles.to_csv(index=False).encode('utf-8')
    st.download_button("Download as CSV", csv, "mobile_phones_dataset.csv", "text/csv")
with col2:
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        mobiles.to_excel(writer, index=False, sheet_name='MobilePhones')
    excel_data = output.getvalue()
    st.download_button("Download as Excel", excel_data, "mobile_phones_dataset.xlsx",
                       "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

st.markdown("---")

# ----- FILTERS -----
st.sidebar.header("Filters")

selected_countries = st.sidebar.multiselect(
    "Select Countries", options=sorted(mobiles["popular_country"].unique()),
    default=sorted(mobiles["popular_country"].unique())
)
selected_companies = st.sidebar.multiselect(
    "Select Brands", options=sorted(mobiles["company_name"].unique()),
    default=sorted(mobiles["company_name"].unique())
)
selected_storage = st.sidebar.multiselect(
    "Select Storage (GB)", options=sorted(mobiles["storage_gb"].unique()),
    default=sorted(mobiles["storage_gb"].unique())
)
selected_battery = st.sidebar.slider(
    "Battery Capacity (mAh)",
    int(mobiles['battery_capacity_mah'].min()), int(mobiles['battery_capacity_mah'].max()),
    (int(mobiles['battery_capacity_mah'].min()), int(mobiles['battery_capacity_mah'].max()))
)
selected_screen = st.sidebar.slider(
    "Screen Size (inches)",
    float(mobiles['screen_size_inches'].min()), float(mobiles['screen_size_inches'].max()),
    (float(mobiles['screen_size_inches'].min()), float(mobiles['screen_size_inches'].max()))
)

filtered_mobiles = mobiles[
    (mobiles["popular_country"].isin(selected_countries)) &
    (mobiles["company_name"].isin(selected_companies)) &
    (mobiles["storage_gb"].isin(selected_storage)) &
    (mobiles["battery_capacity_mah"] >= selected_battery[0]) &
    (mobiles["battery_capacity_mah"] <= selected_battery[1]) &
    (mobiles["screen_size_inches"] >= selected_screen[0]) &
    (mobiles["screen_size_inches"] <= selected_screen[1])
]

# ----- MAP CHOROPLETH -----
popularity_by_country = filtered_mobiles.groupby('popular_country')['popularity_%'].mean().reset_index()
popularity_by_country.columns = ['country', 'avg_popularity']

fig = px.choropleth(
    popularity_by_country,
    locations='country',
    locationmode='country names',
    color='avg_popularity',
    hover_name='country',
    color_continuous_scale=px.colors.sequential.Plasma,
    title='Mobile Phone Popularity by Country (%)',
    labels={'avg_popularity': 'Popularity (%)'}
)
fig.update_layout(geo=dict(showframe=False, showcoastlines=True))
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ----- SECTION B: Dials WITHOUT needles, with centered text -----
def create_dial(value, max_value, label, color, unit=""):
    fig, ax = plt.subplots(figsize=(4, 4), subplot_kw={'projection': 'polar'})
    theta = np.linspace(0, 2 * np.pi, 100)
    ax.plot(theta, [max_value] * 100, color='lightgray', linewidth=15, alpha=0.3)
    filled = int((value / max_value) * 100)
    ax.plot(theta[:filled], [max_value] * filled, color=color, linewidth=15, alpha=0.7)
    ax.text(0, 0, f"{value}{unit}", ha='center', va='center', fontsize=22, fontweight='bold', color=color)
    ax.set_title(label, pad=15)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_ylim(0, max_value * 1.2)
    plt.tight_layout()
    return fig

st.title("📊 Top Phones Summary Dashboard")

popularity_max = filtered_mobiles['popularity_%'].max() if not filtered_mobiles.empty else 100
popularity_val = filtered_mobiles['popularity_%'].max() if not filtered_mobiles.empty else 0
popularity_label = "Popularity"

power_max = filtered_mobiles['benchmark_score'].max() if not filtered_mobiles.empty else 150000
power_val = filtered_mobiles['benchmark_score'].max() if not filtered_mobiles.empty else 0
power_label = "Benchmark Score"

battery_max = filtered_mobiles['battery_capacity_mah'].max() if not filtered_mobiles.empty else 6000
battery_val = filtered_mobiles['battery_capacity_mah'].max() if not filtered_mobiles.empty else 0
battery_label = "Battery Capacity"

col1, col2, col3 = st.columns(3)
with col1:
    st.pyplot(create_dial(popularity_val, popularity_max, popularity_label, '#2ecc71', '%'))
with col2:
    st.pyplot(create_dial(power_val, power_max, power_label, '#3498db'))
with col3:
    st.pyplot(create_dial(battery_val, battery_max, battery_label, '#e67e22', ' mAh'))

st.markdown("---")

# Group by company and calculate average popularity
brand_popularity = mobiles.groupby('company_name')['popularity_%'].mean().reset_index()

fig = px.bar(
    brand_popularity,
    x='company_name',
    y='popularity_%',
    title='Average Popularity by Brand',
    labels={'company_name': 'Brand', 'popularity_%': 'Popularity (%)'},
    color='company_name'
)
st.plotly_chart(fig, use_container_width=True)

# ----- SECTION C: Heatmaps & Correlations -----
st.title("🔍 Heatmaps & Correlation Analysis")

image1 = Image.open("heat.png")
st.image(image1, caption="📊 RAM vs Storage Heatmap", use_container_width=True)
with open("heat.png", "rb") as file:
    st.download_button(
        label="📥 Download RAM vs Storage Heatmap",
        data=file,
        file_name="heat.png",
        mime="image/png"
    )




st.markdown("---")

# ----- SECTION E: Gradient Bar Chart with Filter -----
st.subheader("📊 Section E: Price & Performance Gradient Chart (Top 30 Models)")

# Dropdown filter
metric = st.selectbox(
    "Select metric to visualize:",
    ["Price (USD)", "Performance (Antutu)", "Storage (GB)"]
)

# Choose column
if metric == "Price (USD)":
    y_col = "launched_price_usa_usd"
    title = "Top 30 Smartphones by Price (USD)"
    color_scale = "Blues"
elif metric == "Performance (Antutu)":
    y_col = "antutu_score"
    title = "Top 30 Smartphones by Antutu Performance"
    color_scale = "Viridis"
else:
    y_col = "storage_gb"
    title = "Top 30 Smartphones by Storage"
    color_scale = "Oranges"

# Clean and select top 30
top_data = mobiles[['model_name', y_col]].dropna().sort_values(by=y_col, ascending=False).head(30)

# Plot gradient bar
fig_metric = px.bar(
    top_data,
    x='model_name',
    y=y_col,
    color=y_col,
    color_continuous_scale=color_scale,
    title=title,
    labels={y_col: metric, 'model_name': 'Model Name'}
)
fig_metric.update_layout(xaxis_tickangle=45, height=500)
st.plotly_chart(fig_metric, use_container_width=True)


st.markdown("---")

# ----- Additional Scatter Plot: Performance vs Price with Battery Bubble Size -----
st.title("💡 Performance vs Price (Bubble size: Battery Capacity)")

if not filtered_mobiles.empty:
    fig5 = px.scatter(
        filtered_mobiles,
        x="benchmark_score",
        y="launched_price_usa_usd",
        size="battery_capacity_mah",
        color="company_name",
        hover_name="model_name",
        size_max=40,
        labels={
            "benchmark_score": "Benchmark Score (Performance)",
            "launched_price_usa_usd": "Price (USD)",
            "battery_capacity_mah": "Battery Capacity (mAh)"
        },
        title="Performance vs Price with Battery Capacity as Bubble Size"
    )
    st.plotly_chart(fig5, use_container_width=True)
else:
    st.info("No data for scatter plot. Adjust filters.")

st.markdown("---")

# ----- CURVED CARDS WITH UPLOADS -----
st.title("🔎 Quick Facts")

# Static images from local files
def load_local_image_b64(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None

b64_1 = load_local_image_b64("2.png")
b64_2 = load_local_image_b64("3.png")
b64_3 = load_local_image_b64("4.png")


# Find best camera phone, cheapest, most expensive
if not filtered_mobiles.empty:
    best_camera_idx = filtered_mobiles['back_camera_mp'].idxmax()
    best_camera_phone = filtered_mobiles.loc[best_camera_idx]

    cheapest_idx = filtered_mobiles['launched_price_usa_usd'].idxmin()
    cheapest_phone = filtered_mobiles.loc[cheapest_idx]

    expensive_idx = filtered_mobiles['launched_price_usa_usd'].idxmax()
    expensive_phone = filtered_mobiles.loc[expensive_idx]
else:
    best_camera_phone = None
    cheapest_phone = None
    expensive_phone = None

cards_info = [
    {
        "title": "📸 Best Camera Phone",
        "subtitle": f"{best_camera_phone['company_name']} {best_camera_phone['model_name']}" if best_camera_phone is not None else "No data",
        "desc": f"Back Camera: {best_camera_phone['back_camera_mp']} MP" if best_camera_phone is not None else "",
        "b64": b64_1
    },
    {
        "title": "💰 Cheapest Phone",
        "subtitle": f"{cheapest_phone['company_name']} {cheapest_phone['model_name']}" if cheapest_phone is not None else "No data",
        "desc": f"Price: ${cheapest_phone['launched_price_usa_usd']}" if cheapest_phone is not None else "",
        "b64": b64_2
    },
    {
        "title": "🏆 Most Expensive Phone",
        "subtitle": f"{expensive_phone['company_name']} {expensive_phone['model_name']}" if expensive_phone is not None else "No data",
        "desc": f"Price: ${expensive_phone['launched_price_usa_usd']}" if expensive_phone is not None else "",
        "b64": b64_3
    }
]

# Display cards side by side with background images
cols = st.columns(3)
for idx, col in enumerate(cols):
    card = cards_info[idx]
    bg_style = f"background-image: url('data:image/png;base64,{card['b64']}');" if card['b64'] else "background-color: #222;"
    col.markdown(
        f"""
        <div class="card" style="{bg_style}">
            <div class="card-title">{card['title']}</div>
            <div class="card-subtitle">{card['subtitle']}</div>
            <div>{card['desc']}</div>
        </div>
        """, unsafe_allow_html=True
    )




st.subheader("📊 Bonus Chart: Average Launch Price by Year (USD)")

# Calculate average launch price per year
avg_price_by_year = filtered_mobiles.groupby('launched_year', as_index=False)['launched_price_usa_usd'].mean()

# Plot bar chart
fig_diff = px.bar(
    avg_price_by_year,
    x='launched_year',
    y='launched_price_usa_usd',
    title='Average Launch Price per Year (USD)',
    labels={
        'launched_year': 'Launch Year',
        'launched_price_usa_usd': 'Average Price (USD)'
    },
    color='launched_price_usa_usd',
    color_continuous_scale='Tealgrn'
)

fig_diff.update_layout(
    xaxis=dict(dtick=1),
    height=500,
    coloraxis_colorbar=dict(title='Avg Price (USD)')
)

st.plotly_chart(fig_diff, use_container_width=True)






#------- ADDITIONAL------





# Price vs. Benchmark Score (Scatter Plot)
fig = px.scatter(
    mobiles,
    x='launched_price_usa_usd',
    y='benchmark_score',
    color='company_name',
    hover_name='model_name',
    title='Price vs. Performance',
    labels={
        'launched_price_usa_usd': 'Price (USD)',
        'benchmark_score': 'Benchmark Score'
    }
)
st.plotly_chart(fig, use_container_width=True)





# Melt data for front/back camera comparison
camera_data = mobiles.melt(
    id_vars=['model_name', 'company_name'],
    value_vars=['front_camera_mp', 'back_camera_mp'],
    var_name='camera_type',
    value_name='megapixels'
)



#  Camera Comparison (Grouped Bar Chart)
fig = px.bar(
    camera_data,
    x='model_name',
    y='megapixels',
    color='camera_type',
    barmode='group',
    title='Front vs. Back Camera Comparison',
    labels={'model_name': 'Model', 'megapixels': 'Megapixels'}
)
st.plotly_chart(fig, use_container_width=True)






#  Storage Options Analysis (Pie Chart)
storage_counts = mobiles['storage_gb'].value_counts().reset_index()
storage_counts.columns = ['storage_gb', 'count']

fig = px.pie(
    storage_counts,
    names='storage_gb',
    values='count',
    title='Storage Capacity Distribution',
    labels={'storage_gb': 'Storage (GB)'}
)
st.plotly_chart(fig, use_container_width=True)







