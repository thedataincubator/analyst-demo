import streamlit as st
import pandas as pd
from io import StringIO, BytesIO

    
@st.cache()
def load_data(filepath):
    
    conversions = pd.read_excel(filepath, engine='openpyxl', sheet_name='Conversions')

    posts = pd.read_excel(filepath, engine='openpyxl', sheet_name='Posts', index_col=0)
    posts['Date'] = pd.to_datetime(posts['Date'])
    
    return conversions, posts

@st.cache()
def preprocess(conversions, posts):
    melted = conversions.melt(id_vars='influencer', var_name='Date', value_name='Conversions').fillna(0)
    melted['Date'] = pd.to_datetime(melted['Date'])
    
    df = posts.merge(melted, left_on=['Date', 'Influencer'], right_on=['Date', 'influencer'])
    df['month'] = df['Date'].dt.strftime('%B %Y')

    return df

def cost_per_acquisition(df):
    if df['Conversions'].sum() > 0:
        return df['Cost'].sum() / df['Conversions'].sum()


def conversion_rate(df):
    if df['Clicks'].sum() > 0:
        return df['Conversions'].sum() / df['Clicks'].sum()
    else:
        return None


def generate_report(df, grouping_column):
    cpa = df.groupby(grouping_column).apply(cost_per_acquisition).rename('CPA').to_frame()
    conv = df.groupby(grouping_column).apply(conversion_rate).rename('Conversion Rate').to_frame()
    sums = df.groupby(grouping_column)[['Cost', 'Clicks', 'Conversions']].sum()
    num_posts = df.groupby(grouping_column).apply(len).rename('Number of Posts').to_frame()
    
    
    out = num_posts.join(sums).join(conv).join(cpa)
    return out

def write_report_to_bytes(conversions, posts):
    
    df = preprocess(conversions, posts)
    
    by_influencer = generate_report(df, ['Influencer'])
    by_month = generate_report(df, ['month'])
    by_influencer_and_month = generate_report(df, ['Influencer', 'month'])
     
    output = BytesIO()
    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter(output, engine='openpyxl')
    
    # Write each dataframe to a different worksheet.
    
    by_influencer.to_excel(writer, sheet_name='Report - Influencer')
    by_month.to_excel(writer, sheet_name='Report - Month')
    by_influencer_and_month.to_excel(writer, sheet_name='Report - Influencer and Month')
    
    # Close the Pandas Excel writer and output the Excel file.
    writer.save()


st.title("Influencer Marketing Report")

st.header("About")

st.markdown('''
This is an interactive application that for generating a report for a synthetic dataset of influencer marketing metrics. 

The tool below excepts an Excel file with the following worksheets:
* *Posts*: This is a table with information on sponsored posts by different influencers. Each row represents one post, and contains the following columns:
    * Date
    * Influencer: A name of an influencer (E.g. Rachel Kelly). In the dataset, these were synthetically generated.
    * Followers: The number of followers that influencer has
    * Follower group: This bins each influencer into one of three groups based on how many followers they have.
    * Cost: The cost for that particular post.
    * Likes
    * Comments
    * Shares
    * Clicks
* Conversions: This is a pivot table. It has one column labeled `"influencer"`, with values matching the influencer names in `Posts`, and the remaining columns correspond to dates. The cell values denote the number of conversions (e.g. sales) attributed to an influencer on a particular day.

### Report outputs

This report uses the input Excel file to compute the following metrics:
* Cost-per-acquisition: How many dollars do we pay per conversion? This is the total marketing spend divided by the number of acquisitions. 
    * Ex: we spend $500 on sponsored posts. Four people click through those posts and end up making a purchase. We spent $125 per conversion.
* Conversion Rate: What proportion of *click* events actually lead to a conversion? 
    * If 100 people click through to our website, but only 3 of them make a purchase, then our conversion rate is 3%.
''')


st.header("Generate Report")

excel_sheet = st.file_uploader('Upload your Excel file.', type=['xls', 'xlsx'])
if not excel_sheet: 
    st.stop()
conversions, posts = load_data(excel_sheet)



df = preprocess(conversions, posts)
report = generate_report(df, 'Influencer')

st.subheader("Report:")
report 

post_section = st.beta_expander("View the raw data")
with post_section:
    st.subheader("Posts")
    posts
    st.subheader("Conversions")
    conversions
