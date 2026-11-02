import streamlit as st
import pandas as pd
import time
from src.model import predict_texts

st.set_page_config(page_title="AI Text Classifier", layout="wide")

st.title("텍스트 분류 프로토타입")
st.caption("Streamlit을 활용한 AI 예측 파이프라인 예시")

texts = st.text_area("문장을 입력하세요 (한 줄당 1문장)", "good\nbad\nawesome")

if st.button("예측 실행"):
    start = time.perf_counter()

    input_texts = [t for t in texts.split("\n") if t.strip()]
    df = predict_texts(input_texts)

    st.success(" 예측 완료!")
    st.dataframe(df)

    # 확률 시각화
    st.bar_chart(df.set_index("text")["prob"])

    # 예측 결과 로그 저장
    df["timestamp"] = pd.Timestamp.now()
    df.to_csv("data/log.csv", mode="a", index=False, header=False)

    elapsed = time.perf_counter() - start
    st.info(f"처리 시간: {elapsed:.3f}초")