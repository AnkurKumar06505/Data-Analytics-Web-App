import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title='Data Analysis Portal',
    page_icon ='🥇'
)

#title
st.title(":red[Data] Analytics Portal")
st.subheader(':red[Explore Data with ease.]',divider='rainbow')
file = st.file_uploader('Drop csv or excel file',type=['csv','xlsx'])
if file != None:
    if (file.name.endswith('csv')):
        data = pd.read_csv(file)
    elif (file.name.endswith('xlsx')):
        file = pd.read_excel(file)
    else: 
        print("The format of the file you uploaded is not of the supported format")
    
    st.dataframe(data)
    st.info("File is succesfully uploaded",icon='🚨')

    st.subheader(':red[Basic information of the datasetset]',divider='rainbow')
    tab1,tab2,tab3,tab4 = st.tabs(['Summary','Top and Bottom Rows','Data types','Columns'])

    with tab1:
        st.write(f'There are {data.shape[0]} Rows and {data.shape[1]} Columns in the dataset')
        st.subheader(":gray[Statistical summary of the dataset]")
        st.dataframe(data.describe())

    with tab2:
        st.subheader(":gray[Top Rows]")
        Toprows = st.slider('Number of rows you want',1,data.shape[0],key='Topslider')
        st.dataframe(data.head(Toprows))

        st.subheader(":gray[Bottom Rows]")
        Bottomrows = st.slider('Number of rows you want',1,data.shape[0],key='bottomslider')
        st.dataframe(data.tail(Bottomrows))

    with tab3:
        st.subheader(':gray[Data Type of columns]')
        st.dataframe(data.dtypes)

    with tab4:
        st.subheader(":gray[Columns]")
        st.dataframe(list(data.columns))

    st.subheader(":red[Column Values to Count]",divider='rainbow')
    with st.expander("Value Count"):
        column = st.selectbox("Choose Column name",options=list(data.columns))
        Toprows = st.number_input('Top rows', min_value=1,step=1)
        count = st.button('Count')
        if(count==True):
            result = data[column].value_counts().reset_index().head(Toprows)
            st.dataframe(result)
            st.subheader("Visualizations",divider='gray')
            fig = px.bar(data_frame = result,x = column, y = 'count',text='count')
            st.plotly_chart(fig)

            fig = px.line(data_frame=result,x=column,y='count',text = 'count',template = 'simple_white')
            st.plotly_chart(fig)

            fig = px.pie(data_frame=result,names=column,values='count')
            st.plotly_chart(fig)

    st.subheader(':red[Groupby : Simplify your data]',divider='rainbow')
    st.write("The Groupby lets you summarize data by specific categories and groups")

    with st.expander("Group by your columns"):
        col1,col2,col3 = st.columns(3)
        with col1:
            groupby_cols = st.multiselect("Choose your column to groupby", options = list(data.columns))

        with col2:
            operation_col = st.selectbox("Choose column for operation",options = list(data.columns))
        
        with col3:
            operation = st.selectbox("Choose operation",options = ['sum','min','max','mean','median','count'])

        if groupby_cols: 
          
          newcol_name = (f"{operation}_{operation_col}")

          result = data.groupby(groupby_cols).agg(**{newcol_name: (operation_col,operation)}).reset_index()
          st.dataframe(result)

          st.subheader(':gray[Data Visualizations]',divider = 'gray')
          graphs = st.selectbox('Choose your graphs',options=['line','bar','scatter','pie','sunburst'])

          if (graphs == 'line'):
              x_axis = st.selectbox('Choose X axis',options = list(result.columns))
              y_axis = st.selectbox('Choose Y axis',options = list(result.columns))
              color = st.selectbox('Choose the color',options=[None] + list(result.columns))
              fig = px.line(data_frame=result,x=x_axis,y=y_axis,color= color,markers='o')
              st.plotly_chart(fig)

          elif (graphs=='bar'):
              x_axis = st.selectbox('Choose X axis',options = list(result.columns))
              y_axis = st.selectbox('Choose Y axis',options = list(result.columns))
              color = st.selectbox('Choose the color',options=[None] + list(result.columns))
              facet_col = st.selectbox('Column Information',options = [None] + list(result.columns))

              fig = px.bar(data_frame=result,x = x_axis,y=y_axis,color=color,facet_col= facet_col)
              st.plotly_chart(fig)

          elif (graphs=='scatter'):
              x_axis = st.selectbox('Choose X axis',options = list(result.columns))
              y_axis = st.selectbox('Choose Y axis',options = list(result.columns))
              color = st.selectbox('Choose the color',options=[None] + list(result.columns))
              size = st.selectbox('Select Column for Size',options=[None]+list(result.columns))
              fig = px.scatter(data_frame=result,x=x_axis,y=y_axis,color=color,size=size)
              st.plotly_chart(fig)

          elif (graphs == 'pie'):
              values = st.selectbox('Choose numerical Values',options=list(result.columns))
              names = st.selectbox('Choose labels',options=list(result.columns))
              fig = px.pie(data_frame=result,values=values,names=names)
              st.plotly_chart(fig)

          elif (graphs=='sunburst'):
              path = st.multiselect('Choose your path',options=list(result.columns))
              fig = px.sunburst(data_frame=result,path = path,values = newcol_name)
              st.plotly_chart(fig)


        else:
            st.warning("Please select at least one column to group by.")

          




        


