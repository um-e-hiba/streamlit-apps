# Import
import streamlit as st
import pandas as pd


st.set_page_config("🧠 Growth Minset")
st.title("🧠 Growth Minset")

st.write("In a growth mindset, people believe that their most basic abilities can be developed through " \
"dedication and hard work—brains and talent are just the starting point. This view creates a love of " \
"learning and a resilience that is essential for great accomplishment.")
st.subheader("What is a growth mindset?")
st.markdown("""A growth mindset means that you thrive on challenge, and don’t see failure as a way 
            to describe yourself but as a springboard for growth and developing your abilities. 
            Your intelligence and talents are all susceptible to growth.
            Simply put, this mindset means that you believe in your ability to become better through
             hard work, and help from others.""")

st.write("**People with a growth mindset say things like:**")
st.write("*“I can't do this... yet.”*")
st.write("*“What can I learn from this?”*")

st.write("**How to develop a growth mindset?**")
st.caption(":blue[1.] Listen to the mindset voice inside of you.")
st.write("Your inner voice like “What if you fail?” or “If you don’t try, nobody will see you fail,” " \
"means you have a fixed mindset voice inside. It’s important to listen to your internal mindset voice " \
"so you can truly discover what type of mindset you have. This is the first step to successfully changing" \
" your mindset.")
st.divider()

st.caption(":blue[2.] Recognize that you have a choice.")
st.write("You understand the mindset voice inside of you is telling you not to try, to protect yourself\
          from failure. Now, the choice is up to you. Will you listen to the voice?")
st.divider()

st.caption(":blue[3.] Talk back with a growth mindset voice.")
st.write("Instead of falling for the fixed mindset voice, talk back to your inner voice with a new \
         mindset. Say things like, “I’m not sure I can do it, but it will be worth it to try.” or \
         “If I don’t try at all, it is a failure. There’s no dignity in that.” This new voice will help \
         you drown out the fixed mindset voice that is crowding your thoughts and ambition.")
st.divider()

st.caption(":blue[4.] Practice.")
st.write("Put yourself in situations that are challenging to help you practice your new voice. With new\
          challenges around every corner, there’s many opportunities to thrive from setbacks and trials.")
st.divider()

st.caption(":blue[5.] Find outside help.")
st.write("Cultivating a growth mindset isn’t something that can be done alone. You’ll need outside\
          help to offer encouragement and advice.")
st.divider()

st.caption(":blue[6.] Stop seeking approval of others.")
st.write("hile you need outside help, you also need to stop worrying about the approval of others. \
         Comparing yourself to others, focusing on how you look to others, and hiding failures are all \
         hindering you from developing a growth mindset, and finding success. Keep focusing on yourself \
         and how you can grow, and stop worrying if others are looking at your progress. Chances are, \
         nobody is.")
st.divider()

st.caption(":blue[7.] Replace the word “failing” with “learning.”")
st.write("As you come to recognize that failing is just a new way of learning, you’ll stop being so \
         afraid of it. By embracing failure as an opportunity to continue learning and growing, you’ll \
         be on your way to understanding what a growth mindset is really all about.")
st.divider()

st.caption(":blue[8.] Take growth mindset action.")
st.write("You need to follow through on the actions your new mindset voice tells you to take on. \
         Sometimes, you may not succeed. But that’s ok. As you practice talking to yourself with a \
         growth mindset, and follow through on the actions, you’ll cultivate the mindset of growth that\
          you desire over time.")
st.divider()

st.markdown("***Set Your Mantra to keep going***")

st.caption("Not perfect. Just better than yesterday.")
st.write("-> A reminder that small steps still move you forward.")

st.caption("Every expert was once a beginner who didn’t quit.")
st.write("-> You're not late — you're on the journey.")

st.caption("I’m not failing. I’m learning.")
st.write("-> Flip the narrative. Mistakes = growth in disguise.")

st.caption("I can do hard things.")
st.write("-> Short. Powerful. True.")

st.caption("I’m building the skills I once thought I couldn’t.")
st.write("->  A reminder that your future self will thank you.")

st.caption("Discomfort is my cue — that means I’m growing.")
st.write("->  If it’s hard, that’s the zone where growth happens.")

st.markdown("*I don’t need to rush — I’m here to grow, not to prove.*")

txt = st.text_area("Would like to hear your thoughts",)
if st.button("Submit"):
    st.write("Alright, we’ll leave it here. Appreciate the insight!")