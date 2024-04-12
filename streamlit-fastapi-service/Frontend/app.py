import streamlit as st
from airflow_helper_functions import process_pdf, fetch_updates
from rag_helper_functions import eval1_exec,eval2_exec
from snowflake_req import fetch_run_res
import pandas as pd

def eval1():
    st.title("Evaluate technique - Using QA")
    option = st.selectbox(
                'Select a Topic:',
                ('Extensions of Multiple Regression', 'Evaluating Regression Model Fit and Interpreting Model Results', 'Model Misspecification')
            )
    button_clicked = st.button("Evaluate")

    # Check if the button is clicked
    if button_clicked:
        st.write("Button clicked!")
        eval1_exec(option)

def eval2():
    st.title("Evaluate technique - knowledge base")
    option = st.selectbox(
                'Select a Topic:',
                ('Extensions of Multiple Regression', 'Evaluating Regression Model Fit and Interpreting Model Results', 'Model Misspecification')
            )
    if st.button('Evaluate'):
        eval2_exec(option)
def check_status_ui():
    st.title("DAG Status")
    run_id = st.text_input('run_id')
    if run_id:
        fetch_updates(run_id)

def qa_parta():
    st.title("Generate QA")
    url = st.text_input('Enter URL link')
    option = st.selectbox(
                'Select a Topic:',
                ('Extensions of Multiple Regression', 'Evaluating Regression Model Fit and Interpreting Model Results', 'Model Misspecification')
            )
    button_clicked = st.button("Generate")
    if option and button_clicked:
        process_pdf(url,dag_id="question_generate",topic=option)

def knowledge_creation():
    st.title("Knowledge Base Creation")
    url = st.text_input('Enter URL link')
    process_pdf(url,dag_id="knowledge_base", topic='')

def run_results():
    st.title("Evaluation Results")
    technique = st.selectbox("technique", ["all",'qa_approach', 'knowledge_approach'])
    topic = st.selectbox("topic", 
                ("all",'Extensions of Multiple Regression', 'Evaluating Regression Model Fit and Interpreting Model Results', 'Model Misspecification')
                         )
    d1 = fetch_run_res(technique,topic)
    df = pd.DataFrame(d1)
    st.dataframe(df)
    st.title("Summary")
    if topic == 'all' and technique=='all':
        for i in ['qa_approach', 'knowledge_approach']:
            st.title(i)
            k = df[df['technique'] == i]['correct_ans'].mean()
            st.write(f"Average correct answers using this technique is {k}")

    # st.title("Evaluation Results using 2nd technique")
    # metadata = fetch_run_res("methodb")
    # st.dataframe(pd.DataFrame(metadata))


pages = {
    "QA Generate": qa_parta,
    "Knowledge Base Generation": knowledge_creation,
    "Evaluation Using QA": eval1,
    "Evaluation Using Keynote": eval2,
    "Dag Status": check_status_ui,
    "Evaluation Results": run_results
}
def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(pages.keys()))
    pages[selection]()

if __name__ == "__main__":
    main()
