import streamlit as st

st.set_page_config(
    page_title="Learning Style Survey",
    page_icon="🧠",
    layout="wide",
)

st.title("Learning Style Survey")
st.write(
    "이 설문은 학습자가 선호하는 학습 양식을 파악하기 위한 도구입니다. "
    "각 문항에 대해 평소 자신의 행동에 가장 가까운 정도를 선택해 주세요."
)
st.caption("0 = Never, 1 = Rarely, 2 = Sometimes, 3 = Often, 4 = Always")

# 문항 정의: (문항번호, 문항텍스트, 파트, 그룹)
items = [
    # Part 1: HOW I USE MY PHYSICAL SENSES
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
    (19, "I can identify people by their voices (e.g., on the phone).", "Part 1", "B"),
    (20, "When I turn on the TV, I listen to the sound more than I watch the screen.", "Part 1", "B"),

    (21, "I prefer to start doing things rather than checking the directions first.", "Part 1", "C"),
    (22, "I need frequent breaks when I work or study.", "Part 1", "C"),
    (23, "I need to eat something when I read or study.", "Part 1", "C"),
    (24, "If I have a choice between sitting and standing, I’d rather stand.", "Part 1", "C"),
    (25, "I get nervous when I sit still too long.", "Part 1", "C"),
    (26, "I think better when I move around (e.g., pacing or tapping my feet).", "Part 1", "C"),
    (27, "I play with or bite on my pens during lectures.", "Part 1", "C"),
    (28, "Manipulating objects helps me to remember what someone says.", "Part 1", "C"),
    (29, "I move my hands when I speak.", "Part 1", "C"),
    (30, "I draw lots of pictures (doodles) in my notebook during lectures.", "Part 1", "C"),

    # Part 2: HOW I EXPOSE MYSELF TO LEARNING SITUATIONS
    (31, "I learn better when I work or study with others than by myself.", "Part 2", "A"),
    (32, "I meet new people easily by jumping into the conversation.", "Part 2", "A"),
    (33, "I learn better in the classroom than with a private tutor.", "Part 2", "A"),
    (34, "It is easy for me to approach strangers.", "Part 2", "A"),
    (35, "Interacting with lots of people gives me energy.", "Part 2", "A"),
    (36, "I experience things first and then try to understand them.", "Part 2", "A"),

    (37, "I am energized by the inner world (what I’m thinking inside).", "Part 2", "B"),
    (38, "I prefer individual or one-on-one games and activities.", "Part 2", "B"),
    (39, "I have a few interests, and I concentrate deeply on them.", "Part 2", "B"),
    (40, "After working in a large group, I am exhausted.", "Part 2", "B"),
    (41, "When I am in a large group, I tend to keep silent and listen.", "Part 2", "B"),
    (42, "I want to understand something well before I try it.", "Part 2", "B"),

    # Part 3: HOW I HANDLE POSSIBILITIES
    (43, "I have a creative imagination.", "Part 3", "A"),
    (44, "I try to find many options and possibilities for why something happens.", "Part 3", "A"),
    (45, "I plan carefully for future events.", "Part 3", "A"),
    (46, "I like to discover things myself rather than have everything explained to me.", "Part 3", "A"),
    (47, "I add many original ideas during class discussions.", "Part 3", "A"),
    (48, "I am open-minded to new suggestions from my peers.", "Part 3", "A"),

    (49, "I focus on a situation as it is rather than thinking about how it could be.", "Part 3", "B"),
    (50, "I read instruction manuals before using the device.", "Part 3", "B"),
    (51, "I trust concrete facts instead of new, untested ideas.", "Part 3", "B"),
    (52, "I prefer things presented in a step-by-step way.", "Part 3", "B"),
    (53, "I dislike it if my classmate changes the plan for our project.", "Part 3", "B"),
    (54, "I follow directions carefully.", "Part 3", "B"),

    # Part 4: HOW I DEAL WITH AMBIGUITY AND WITH DEADLINES
    (55, "I like to plan language study sessions carefully and do lessons on time or early.", "Part 4", "A"),
    (56, "My notes, handouts, and other school materials are carefully organized.", "Part 4", "A"),
    (57, "I like to be certain about what things mean in a target language.", "Part 4", "A"),
    (58, "I like to know how rules are applied and why.", "Part 4", "A"),

    (59, "I let deadlines slide if I’m involved in other things.", "Part 4", "B"),
    (60, "I let things pile up on my desk to be organized eventually.", "Part 4", "B"),
    (61, "I don’t worry about comprehending everything.", "Part 4", "B"),
    (62, "I don’t feel the need to come to rapid conclusions about a topic.", "Part 4", "B"),

    # Part 5: HOW I RECEIVE INFORMATION
    (63, "I prefer short and simple answers rather than long explanations.", "Part 5", "A"),
    (64, "I ignore details that do not seem relevant.", "Part 5", "A"),
    (65, "It is easy for me to see the overall plan or big picture.", "Part 5", "A"),
    (66, "I get the main idea, and that’s enough for me.", "Part 5", "A"),
    (67, "When I tell an old story, I tend to forget lots of specific details.", "Part 5", "A"),

    (68, "I need very specific examples in order to understand fully.", "Part 5", "B"),
    (69, "I pay attention to specific facts or information.", "Part 5", "B"),
    (70, "I’m good at catching new phrases or words when I hear them.", "Part 5", "B"),
    (71, "I enjoy activities where I fill in the blank with missing words I hear.", "Part 5", "B"),
    (72, "When I try to tell a joke, I remember details but forget the punch line.", "Part 5", "B"),

    # Part 6: HOW I FURTHER PROCESS INFORMATION
    (73, "I can summarize information easily.", "Part 6", "A"),
    (74, "I can quickly paraphrase what other people say.", "Part 6", "A"),
    (75, "When I create an outline, I consider the key points first.", "Part 6", "A"),
    (76, "I enjoy activities where I have to pull ideas together.", "Part 6", "A"),
    (77, "By looking at the whole situation, I can easily understand someone.", "Part 6", "A"),

    (78, "I have a hard time understanding when I don’t know every word.", "Part 6", "B"),
    (79, "When I tell a story or explain something, it takes a long time.", "Part 6", "B"),
    (80, "I like to focus on grammar rules.", "Part 6", "B"),
    (81, "I’m good at solving complicated mysteries and puzzles.", "Part 6", "B"),
    (82, "I am good at noticing even the smallest details involved in a task.", "Part 6", "B"),

    # Part 7: HOW I COMMIT MATERIAL TO MEMORY
    (83, "I try to pay attention to all the features of new material as I learn.", "Part 7", "A"),
    (84, "When I memorize different bits of language material, I can retrieve these bits easily.", "Part 7", "A"),
    (85, "As I learn new material in the target language, I make fine distinctions among sounds, forms, and words.", "Part 7", "A"),

    (86, "When learning new information, I may clump together data by eliminating or reducing differences.", "Part 7", "B"),
    (87, "I ignore distinctions that would make what I say more accurate in the given context.", "Part 7", "B"),
    (88, "Similar memories become blurred in my mind; I merge new learning experiences with previous ones.", "Part 7", "B"),

    # Part 8: HOW I DEAL WITH LANGUAGE RULES
    (89, "I like to go from general patterns to specific examples in learning a target language.", "Part 8", "A"),
    (90, "I like to start with rules and theories rather than specific examples.", "Part 8", "A"),
    (91, "I like to begin with generalizations and then find experiences that relate to those generalizations.", "Part 8", "A"),

    (92, "I like to learn rules of language indirectly by being exposed to examples.", "Part 8", "B"),
    (93, "I don’t really care if I hear a rule stated since I don’t remember rules very well anyway.", "Part 8", "B"),
    (94, "I figure out rules based on the way I see language forms behaving over time.", "Part 8", "B"),

    # Part 9: HOW I DEAL WITH MULTIPLE INPUTS
    (95, "I can separate out the relevant and important information even when distracting information is present.", "Part 9", "A"),
    (96, "When I produce an oral or written message, I make sure that all grammatical structures are in agreement.", "Part 9", "A"),
    (97, "I not only attend to grammar but check for appropriate levels of formality and politeness.", "Part 9", "A"),

    (98, "When speaking or writing, I feel that focusing on grammar is less important than paying attention to content.", "Part 9", "B"),
    (99, "It is a challenge for me to focus on communication while paying attention to grammatical agreement.", "Part 9", "B"),
    (100, "When I am using lengthy sentences, I get distracted and neglect aspects of grammar and style.", "Part 9", "B"),

    # Part 10: HOW I DEAL WITH RESPONSE TIME
    (101, "I react quickly in language situations.", "Part 10", "A"),
    (102, "I go with my instincts in the target language.", "Part 10", "A"),
    (103, "I jump in, see what happens, and make corrections if needed.", "Part 10", "A"),

    (104, "I need to think things through before speaking or writing.", "Part 10", "B"),
    (105, "I like to look before I leap when determining what to say or write.", "Part 10", "B"),
    (106, "I attempt to find supporting material in my mind before producing language.", "Part 10", "B"),

    # Part 11: HOW LITERALLY I TAKE REALITY
    (107, "I find that building metaphors in my mind helps me deal with language.", "Part 11", "A"),
    (108, "I learn things through metaphors and associations with other things.", "Part 11", "A"),

    (109, "I take learning language literally and don’t deal in metaphors.", "Part 11", "B"),
    (110, "I take things at face value, so I like language material that says what it means directly.", "Part 11", "B"),
]

# 각 파트-그룹이 의미하는 스타일 이름
style_labels = {
    ("Part 1", "A"): ("Visual", "시각적 학습: 그림, 글, 도표 등 눈으로 보는 정보를 선호합니다."),
    ("Part 1", "B"): ("Auditory", "청각적 학습: 듣기, 토론, 강의 등을 통해 배우는 것을 선호합니다."),
    ("Part 1", "C"): ("Tactile/Kinesthetic", "촉각·운동 감각 학습: 몸을 움직이고 직접 해 보면서 배우는 것을 선호합니다."),

    ("Part 2", "A"): ("Extroverted", "외향적: 사람들과 함께 활동하고 상호작용하면서 배우는 것을 선호합니다."),
    ("Part 2", "B"): ("Introverted", "내향적: 혼자 또는 소수와 조용히 작업하면서 배우는 것을 선호합니다."),

    ("Part 3", "A"): ("Random-Intuitive", "직관·가능성 지향: 미래, 가능성, 아이디어 탐색을 좋아합니다."),
    ("Part 3", "B"): ("Concrete-Sequential", "구체·순차 지향: 현재, 단계별 설명, 매뉴얼 등을 선호합니다."),

    ("Part 4", "A"): ("Closure-Oriented", "마감·구조 지향: 계획 세우기, 마감 준수, 명확한 지시를 선호합니다."),
    ("Part 4", "B"): ("Open", "개방적: 여유 있게 배우고, 발견 학습과 융통성을 선호합니다."),

    ("Part 5", "A"): ("Global", "전체적: 큰 그림과 요지를 빨리 파악하는 것을 선호합니다."),
    ("Part 5", "B"): ("Particular", "세부적: 구체적인 예, 세부 정보에 주의를 기울입니다."),

    ("Part 6", "A"): ("Synthesizing", "통합적: 요약, 재구성, 의미 추론을 잘합니다."),
    ("Part 6", "B"): ("Analytic", "분석적: 문법 규칙, 세부 분석, 논리적인 구분에 강점이 있습니다."),

    ("Part 7", "A"): ("Sharpener", "구분형: 세밀한 차이를 잘 구분하고 개별적으로 기억합니다."),
    ("Part 7", "B"): ("Leveler", "통합형: 비슷한 정보들을 묶어서 큰 덩어리로 기억합니다."),

    ("Part 8", "A"): ("Deductive", "연역적: 규칙과 이론에서 시작해서 예로 내려오는 것을 선호합니다."),
    ("Part 8", "B"): ("Inductive", "귀납적: 예와 사용 사례를 보면서 자연스럽게 규칙을 발견하는 것을 선호합니다."),

    ("Part 9", "A"): ("Field-Independent", "맥락 분리형: 주변 방해 속에서도 핵심 정보를 뽑아내는 능력이 강합니다."),
    ("Part 9", "B"): ("Field-Dependent", "맥락 의존형: 전체 맥락과 분위기를 함께 느끼며 이해하는 경향이 있습니다."),

    ("Part 10", "A"): ("Impulsive", "충동형: 빠르게 반응하고 먼저 시도해 보며 조정하는 스타일입니다."),
    ("Part 10", "B"): ("Reflective", "숙고형: 말하거나 쓰기 전에 충분히 생각한 후 행동하는 스타일입니다."),

    ("Part 11", "A"): ("Metaphoric", "은유적: 비유, 이미지, 연결고리를 통해 개념을 이해하는 것을 선호합니다."),
    ("Part 11", "B"): ("Literal", "직설적: 문자 그대로의 뜻과 직접적인 설명을 선호합니다."),
}

# Streamlit 폼
with st.form("survey_form"):
    responses = {}
    current_part = None

    for num, text, part, group in items:
        if part != current_part:
            st.markdown(f"### {part}")
            current_part = part

        key = f"item_{num}"
        responses[key] = st.slider(
            f"{num}. {text}",
            min_value=0,
            max_value=4,
            value=2,
            step=1,
            key=key,
        )

    submitted = st.form_submit_button("결과 보기")

if submitted:
    # 파트-그룹별 합산
    part_group_totals = {}
    for (num, text, part, group) in items:
        key = f"item_{num}"
        value = responses.get(key, 0)
        part_group_totals.setdefault(part, {}).setdefault(group, 0)
        part_group_totals[part][group] += value

    st.subheader("나의 학습 양식 결과")

    for part, groups in part_group_totals.items():
        # 가장 높은 점수 찾기
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
    "각 문항에 대해 평소 자신의 행동을 가장 잘 나타내는 숫자를 선택한 후 "
    "[결과 보기] 버튼을 눌러 주세요."
)
st.sidebar.write("0 = Never, 1 = Rarely, 2 = Sometimes, 3 = Often, 4 = Always")
