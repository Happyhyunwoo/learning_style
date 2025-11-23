import streamlit as st

st.set_page_config(
    page_title="Learning Style Survey",
    page_icon="🧠",
    layout="wide",
)

st.title("Learning Style Survey")
st.write(
    "이 설문은 학습자가 선호하는 학습 양식을 파악하기 위한 도구입니다. "
    "각 문항에 대해 평소 자신의 행동에 가장 가까운 항목을 선택해 주세요."
)
st.caption("1 = Never, 2 = Rarely, 3 = Sometimes, 4 = Often")

# 문항 정의: (문항번호, 문항텍스트, 파트, 그룹)
# 전체 문항(items)은 그대로 사용 (생략)
# 기존에 드린 코드의 items 리스트를 그대로 붙여 넣으시면 됩니다.

items = [
    # 예시 (전체 문항은 이전 메시지에서 그대로 가져오세요)
    (1, "I remember something better if I write it down.", "Part 1", "A"),
    (2, "I take detailed notes during lectures.", "Part 1", "A"),
    # ... 생략 ...
    (110, "I take things at face value, so I like language material that says what it means directly.", "Part 11", "B"),
]

# 스타일 이름
style_labels = {
    # ... 기존 내용 유지 ...
}

with st.form("survey_form"):
    responses = {}
    current_part = None

    for num, text, part, group in items:
        if part != current_part:
            st.markdown(f"### {part}")
            current_part = part

        key = f"item_{num}"
        responses[key] = st.radio(
            f"{num}. {text}",
            options=[1, 2, 3, 4],
            index=2,
            horizontal=True,
            key=key
        )

    submitted = st.form_submit_button("결과 보기")

if submitted:
    part_group_totals = {}
    for (num, text, part, group) in items:
        key = f"item_{num}"
        value = responses.get(key, 1)
        part_group_totals.setdefault(part, {}).setdefault(group, 0)
        part_group_totals[part][group] += value

    st.subheader("나의 학습 양식 결과")

    for part, groups in part_group_totals.items():
        max_score = max(groups.values())
        best_groups = [g for g, v in groups.items() if v == max_score]

        st.markdown(f"#### {part}")
        score_text = ", ".join([f"{g}: {groups[g]}" for g in sorted(groups.keys())])
        st.write(f"점수: {score_text}")

        label_texts = []
        for g in best_groups:
            label, desc = style_labels.get((part, g), (None, None))
            if label:
                label_texts.append(f"**{label}** ({g}) – {desc}")

        if label_texts:
            st.write("주요 학습 양식:")
            for t in label_texts:
                st.write(t)
        else:
            st.write("이 파트에 대한 스타일 정보가 정의되어 있지 않습니다.")

    st.info(
        "이 결과는 ‘경향’을 보여 주는 것이며 절대적인 진단이 아닙니다. "
        "상황에 따라 다른 스타일을 보일 수 있고, 연습을 통해 선호하지 않던 스타일도 "
        "발달시킬 수 있습니다."
    )

st.sidebar.header("사용 방법")
st.sidebar.write(
    "각 문항에 대해 1~4 중 하나를 선택한 후 "
    "[결과 보기] 버튼을 눌러 주세요."
)
st.sidebar.write("1 = Never, 2 = Rarely, 3 = Sometimes, 4 = Often")
