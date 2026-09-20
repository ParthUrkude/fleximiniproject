
import streamlit as st

st.set_page_config(
    page_title="Emergency AI Assistant",
    page_icon="🚨",
    layout="centered"
)

# Emergency information database
EMERGENCY_DATA = {
    "fire": {
        "title": "🔥 Fire Emergency",
        "steps": [
            "Leave the building using a safe exit.",
            "Do not use elevators.",
            "Stay low if there is smoke.",
            "Move away from the building once outside."
        ],
        "contact": "Fire: 101 | Emergency: 112"
    },
    "medical": {
        "title": "🚑 Medical Emergency",
        "steps": [
            "Check that the area is safe.",
            "Call emergency services for urgent help.",
            "Follow the dispatcher's instructions.",
            "Avoid giving medication unless advised "
            "by a qualified professional."
        ],
        "contact": "Ambulance: 108 | Emergency: 112"
    },
    "accident": {
        "title": "🚗 Road Accident",
        "steps": [
            "Move to a safe place if possible.",
            "Call emergency services and share the location.",
            "Avoid moving injured people unless there is "
            "immediate danger.",
            "Follow emergency responders' instructions."
        ],
        "contact": "Emergency: 112"
    },
    "earthquake": {
        "title": "🌍 Earthquake",
        "steps": [
            "Drop, cover, and hold on during shaking.",
            "Stay away from windows and heavy objects.",
            "If outdoors, move away from buildings and wires.",
            "After shaking stops, follow official instructions."
        ],
        "contact": "Emergency: 112"
    }
}

# Agent: understand emergency query
def detect_emergency(query):
    query = query.lower()

    keywords = {
        "fire": ["fire", "smoke", "burning", "flames"],
        "medical": [
            "medical", "unconscious", "not breathing",
            "bleeding", "heart attack", "ambulance"
        ],
        "accident": [
            "accident", "crash", "collision"
        ],
        "earthquake": [
            "earthquake", "tremor", "ground shaking"
        ]
    }

    for emergency, words in keywords.items():
        if any(word in query for word in words):
            return emergency

    return None


# Agent: select suitable response
def generate_response(query):
    emergency = detect_emergency(query)

    if emergency is None:
        return {
            "title": "ℹ️ More Information Needed",
            "steps": [
                "Describe what happened.",
                "Mention whether anyone is in danger.",
                "If immediate danger exists, call 112."
            ],
            "contact": "India Emergency Number: 112"
        }

    return EMERGENCY_DATA[emergency]


# User interface
st.title("🚨 Emergency AI Assistant")
st.caption("AI-powered emergency information support")

st.warning(
    "For immediate danger, contact emergency services. "
    "This prototype does not contact responders."
)

with st.form("emergency_form"):
    user_query = st.text_area(
        "Describe your emergency",
        placeholder="Example: There is a fire in my building..."
    )

    submitted = st.form_submit_button(
        "Get Emergency Assistance",
        use_container_width=True
    )

if submitted:
    if not user_query.strip():
        st.error("Please enter an emergency query.")
    else:
        response = generate_response(user_query)

        st.subheader(response["title"])
        st.markdown("### Recommended Safety Steps")

        for step in response["steps"]:
            st.markdown(f"- {step}")

        st.info(response["contact"])

st.divider()
st.caption("Mini Project | Agentic AI & Automation")