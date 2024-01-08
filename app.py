import streamlit as st

st.title("App")
st.header("APP")
st.subheader("app")
st.text("a p p")

st.markdown("**app** *app* app")
st.markdown("# app")
st.caption("app")
st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")
json = {
    "a":"1,2,3",
    "b":"4,5,6"
}
st.json(json)
code = """
print("app")
def f():
    return 0
"""
st.code(code, language="python")


st.write() #всё
