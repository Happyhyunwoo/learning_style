import streamlit as st

st.set_page_config(
    page_title="Learning Style Survey",
    page_icon="🧠",
    layout="wide",
)

st.markdown("""
    <style>
        /* 문항 텍스트 크기 */
        .stRadio > label {
            font-size: 40px !important;
        }

        /* 라디오 선택지 크기 */
        .stRadio div[role='radiogroup'] label {
            font-size: 25px !important;
        }
    </style>
""", unsafe_allow_html=True)

st.title("Learning Style Survey")
st.write(
    "이 설문은 학습자가 선호하는 학습 양식을 파악하기 위한 도구입니다. "
    "각 문항에 대해 평소 자신의 행동에 가장 가까운 항목을 선택해 주세요."
)
st.caption("1 = Never, 2 = Rarely, 3 = Sometimes, 4 = Often")

###############################################################################
# 문항 정의: (문항번호, 문항텍스트, 파트, 그룹)
###############################################################################

items = [
    # Part 1
    (1, "I remember something better if I write it down.", "Part 1", "A"),
    (2, "I take detailed notes during lectures.", "Part 1", "A"),
    (3, "When I listen, I visualize pictures, numbers, or words in my head.", "Part 1", "A"),
    (4, "I prefer to learn with TV or video rather than other media.", "Part 1", "A"),
    (5, "I use color-coding to help me as I learn or work.", "Part 1", "A"),
    (6, "I need written directions for tasks.", "Part 1", "A"),
    (7, "I have to look at people to understand what they say.", "Part 1", "A"),
    (8, "I understand lectures better when professors write on the board.", "Part 1", "A"),
    (9, "Charts, diagrams, and maps help me understand what someone says.", "Part 1", "A"),
    (10, "I remember peoples’ faces but not their names.", "Part 1", "A"),

    (11, "I remember things better if I discuss them with someone.", "Part 1", "B"),
    (12, "I prefer to learn by listening to a lecture rather than reading.", "Part 1", "B"),
    (13, "I need oral directions for a task.", "Part 1", "B"),
    (14, "Background sound helps me think.", "Part 1", "B"),
    (15, "I like to listen to music when I study or work.", "Part 1", "B"),
    (16, "I can understand what people say even when I cannot see them.", "Part 1", "B"),
    (17, "I remember peoples’ names but not their faces.", "Part 1", "B"),
    (18, "I easily remember jokes that I hear.", "Part 1", "B"),
    (19, "I can identify people by their voices.", "Part 1", "B"),
    (20, "When I turn on the TV, I listen to the sound more than I watch the screen.", "Part 1", "B"),

    (21, "I prefer to start doing things rather than checking the directions first.", "Part 1", "C"),
    (22, "I need frequent breaks when I work or study.", "Part 1", "C"),
    (23, "I need to eat something when I read or study.", "Part 1", "C"),
    (24, "If I have a choice between sitting and standing, I’d rather stand.", "Part 1", "C"),
    (25, "I get nervous when I sit still too long.", "Part 1", "C"),
    (26, "I think better when I move around.", "Part 1", "C"),
    (27, "I play with or bite on my pens during lectures.", "Part 1", "C"),
    (28, "Manipulating objects helps me to remember what someone says.", "Part 1", "C"),
    (29, "I move my hands when I speak.", "Part 1", "C"),
    (30, "I draw lots of pictures (doodles) in my notebook during lectures.", "Part 1", "C"),

    # Part 2
    (31, "I learn better when I work with others than by myself.", "Part 2", "A"),
    (32, "I meet new people easily by jumping into the conversation.", "Part 2", "A"),
    (33, "I learn better in the classroom than with a private tutor.", "Part 2", "A"),
    (34, "It is easy for me to approach strangers.", "Part 2", "A"),
    (35, "Interacting with lots of people gives me energy.", "Part 2", "A"),
    (36, "I experience things first and then try to understand them.", "Part 2", "A"),

    (37, "I am energized by the inner world of my thoughts.", "Part 2", "B"),
    (38, "I prefer individual or one-on-one activities.", "Part 2", "B"),
    (39, "I have a few interests that I concentrate deeply on.", "Part 2", "B"),
    (40, "After working in a large group, I am exhausted.", "Part 2", "B"),
    (41, "In a large group, I tend to be silent and listen.", "Part 2", "B"),
    (42, "I want to understand something well before I try it.", "Part 2", "B"),

    # Part 3
    (43, "I have a creative imagination.", "Part 3", "A"),
    (44, "I try to find many possibilities for why something happens.", "Part 3", "A"),
    (45, "I plan carefully for future events.", "Part 3", "A"),
    (46, "I like to discover things myself.", "Part 3", "A"),
    (47, "I add original ideas during discussions.", "Part 3", "A"),
    (48, "I am open-minded to new suggestions.", "Part 3", "A"),

    (49, "I focus on a situation as it is rather than how it could be.", "Part 3", "B"),
    (50, "I read instruction manuals before using a device.", "Part 3", "B"),
    (51, "I trust concrete facts over untested ideas.", "Part 3", "B"),
    (52, "I prefer step-by-step explanations.", "Part 3", "B"),
    (53, "I dislike sudden changes in plans.", "Part 3", "B"),
    (54, "I follow directions carefully.", "Part 3", "B"),

    # Part 4
    (55, "I plan study sessions carefully and finish early.", "Part 4", "A"),
    (56, "My school materials are carefully organized.", "Part 4", "A"),
    (57, "I like to be certain about what things mean.", "Part 4", "A"),
    (58, "I like to know how rules are applied and why.", "Part 4", "A"),

    (59, "I let deadlines slide if I'm involved in other things.", "Part 4", "B"),
    (60, "I let things pile up on my desk.", "Part 4", "B"),
    (61, "I don't worry about comprehending everything.", "Part 4", "B"),
    (62, "I don't feel the need for rapid conclusions.", "Part 4", "B"),

    # Part 5
    (63, "I prefer short and simple answers.", "Part 5", "A"),
    (64, "I ignore details that seem irrelevant.", "Part 5", "A"),
    (65, "It is easy for me to see the big picture.", "Part 5", "A"),
    (66, "I get the main idea, and that’s enough.", "Part 5", "A"),
    (67, "When telling a story, I forget details.", "Part 5", "A"),

    (68, "I need specific examples to understand fully.", "Part 5", "B"),
    (69, "I pay attention to specific information.", "Part 5", "B"),
    (70, "I'm good at catching new phrases when I hear them.", "Part 5", "B"),
    (71, "I enjoy fill-in-the-blank listening activities.", "Part 5", "B"),
    (72, "When telling a joke, I remember details but forget the punchline.", "Part 5", "B"),

    # Part 6
    (73, "I can summarize information easily.", "Part 6", "A"),
    (74, "I can quickly paraphrase others.", "Part 6", "A"),
    (75, "I consider key points first when outlining.", "Part 6", "A"),
    (76, "I enjoy pulling ideas together.", "Part 6", "A"),
    (77, "Looking at the whole helps me understand others.", "Part 6", "A"),

    (78, "I struggle when I don’t know every word.", "Part 6", "B"),
    (79, "I take a long time to explain things.", "Part 6", "B"),
    (80, "I focus on grammar rules.", "Part 6", "B"),
    (81, "I'm good at solving puzzles.", "Part 6", "B"),
    (82, "I notice even small details.", "Part 6", "B"),

    # Part 7
    (83, "I pay attention to all features of new material.", "Part 7", "A"),
    (84, "I can retrieve memorized material easily.", "Part 7", "A"),
    (85, "I notice fine differences among sounds, forms, and words.", "Part 7", "A"),

    (86, "I group similar information together.", "Part 7", "B"),
    (87, "I ignore fine distinctions to simplify learning.", "Part 7", "B"),
    (88, "Similar memories merge in my mind.", "Part 7", "B"),

    # Part 8
    (89, "I like going from general patterns to specific examples.", "Part 8", "A"),
    (90, "I prefer starting with rules and theories.", "Part 8", "A"),
    (91, "I begin with generalizations and find matching experiences.", "Part 8", "A"),

    (92, "I like learning rules indirectly through examples.", "Part 8", "B"),
    (93, "I don’t care much for stated rules.", "Part 8", "B"),
    (94, "I figure out rules by observing language over time.", "Part 8", "B"),

    # Part 9
    (95, "I can pick out relevant information despite distractions.", "Part 9", "A"),
    (96, "I make sure all grammatical structures match.", "Part 9", "A"),
    (97, "I check both grammar and levels of politeness.", "Part 9", "A"),

    (98, "Content is more important than grammar.", "Part 9", "B"),
    (99, "It's hard to focus on communication and grammar at once.", "Part 9", "B"),
    (100, "Long sentences distract me from grammar.", "Part 9", "B"),

    # Part 10
    (101, "I react quickly in language situations.", "Part 10", "A"),
    (102, "I go with my instincts.", "Part 10", "A"),
    (103, "I jump in first and correct later.", "Part 10", "A"),

    (104, "I need to think before speaking or writing.", "Part 10", "B"),
    (105, "I like to ‘look before I leap’.", "Part 10", "B"),
    (106, "I gather supporting material before producing language.", "Part 10", "B"),

    # Part 11
    (107, "Metaphors help me understand language.", "Part 11", "A"),
    (108, "I learn through metaphors and associations.", "Part 11", "A"),

    (109, "I take language literally and avoid metaphors.", "Part 11", "B"),
    (110, "I prefer language that says exactly what it means.", "Part 11", "B"),
]

###############################################################################
# 각 파트-그룹 → 학습 스타일 이름
###############################################################################

style_labels = {
    ("Part 1", "A"): ("Visual", "시각적 학습자입니다."),
    ("Part 1", "B"): ("Auditory", "청각적 학습자입니다."),
    ("Part 1", "C"): ("Tactile/Kinesthetic", "운동·촉각 중심 학습자입니다."),

    ("Part 2", "A"): ("Extroverted", "외향적 학습 성향입니다."),
    ("Part 2", "B"): ("Introverted", "내향적 학습 성향입니다."),

    ("Part 3", "A"): ("Random-Intuitive", "직관적·창의적 학습 성향입니다."),
    ("Part 3", "B"): ("Concrete-Sequential", "구체적·순차적 학습 성향입니다."),

    ("Part 4", "A"): ("Closure-Oriented", "구조·마감 중심 성향입니다."),
    ("Part 4", "B"): ("Open", "개방적·유연한 성향입니다."),

    ("Part 5", "A"): ("Global", "큰 그림 중심 사고입니다."),
    ("Part 5", "B"): ("Particular", "세부 정보 중심 사고입니다."),

    ("Part 6", "A"): ("Synthesizing", "통합적 처리 성향입니다."),
    ("Part 6", "B"): ("Analytic", "분석적 처리 성향입니다."),

    ("Part 7", "A"): ("Sharpener", "정보를 세밀하게 구분합니다."),
    ("Part 7", "B"): ("Leveler", "정보를 묶어 전체적으로 이해합니다."),

    ("Part 8", "A"): ("Deductive", "연역적 학습 성향입니다."),
    ("Part 8", "B"): ("Inductive", "귀납적 학습 성향입니다."),

    ("Part 9", "A"): ("Field-Independent", "맥락과 독립적으로 정보 파악을 잘합니다."),
    ("Part 9", "B"): ("Field-Dependent", "전체 맥락을 함께 고려하는 편입니다."),

    ("Part 10", "A"): ("Impulsive", "빠르고 직관적으로 반응하는 편입니다."),
    ("Part 10", "B"): ("Reflective", "신중하고 숙고한 뒤 반응합니다."),

    ("Part 11", "A"): ("Metaphoric", "비유적 이해를 선호합니다."),
    ("Part 11", "B"): ("Literal", "직설적 표현을 선호합니다."),
}

###############################################################################
# Streamlit Form
###############################################################################

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
            index=None,             # ← 기본 선택 없음
            horizontal=True,
            key=key
        )

    submitted = st.form_submit_button("결과 보기")

###############################################################################
# 채점 및 결과 출력
###############################################################################

if submitted:
    part_group_totals = {}

    for (num, text, part, group) in items:
        key = f"item_{num}"
        value = responses.get(key)

        if value is None:
            st.error(f"{num}번 문항이 선택되지 않았습니다.")
            st.stop()

        part_group_totals.setdefault(part, {}).setdefault(group, 0)
        part_group_totals[part][group] += value

    st.subheader("나의 학습 양식 결과")

    for part, groups in part_group_totals.items():
        max_score = max(groups.values())
        best = [g for g, v in groups.items() if v == max_score]

        st.markdown(f"#### {part}")
        st.write(", ".join([f"{g}: {groups[g]}" for g in sorted(groups.keys())]))

        for g in best:
            label, desc = style_labels.get((part, g), ("Unknown", ""))
            st.write(f"**{label} ({g})** – {desc}")

    st.info(
        "이 결과는 경향성을 보여주는 참고 자료이며, 절대적인 진단이 아닙니다. "
        "상황에 따라 다양한 학습 스타일을 사용할 수 있습니다."
    )

###############################################################################
# Sidebar
###############################################################################

st.sidebar.header("사용 방법")
st.sidebar.write(
    "각 문항에 대해 1~4 중 하나를 선택한 후 [결과 보기] 버튼을 눌러 주세요."
)
st.sidebar.write("1 = Never, 2 = Rarely, 3 = Sometimes, 4 = Often")
