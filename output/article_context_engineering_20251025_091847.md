# Stanford's Practical Guide to 10x Your AI Productivity: The Context Engineering Revolution

I joke that AI is bad software but it's good people. This simple insight has fundamentally changed how I approach artificial intelligence, and it should change how you think about it too.

A good friend of mine was trying to build a tool that would help him with his construction business. He asked ChatGPT if it could help, and of course it said absolutely—let's work on this together—and starts creating a plan. Then it got to the point that ChatGPT said "check back in a couple of days and I'll have it together." My friend asked me, "Is it normal for ChatGPT to ask me to check back in a couple days?" I just started laughing because I hear this all the time from people.

People hear from AI, "Check back in 15 minutes." If AI tells you that, it means it doesn't want to say, "I can't do it." The large language model has been instructed in certain ways to behave in certain ways, but you have to know at its basic level, AI wants to be helpful. And so it's predisposed to say yes. It's a super eager, super enthusiastic intern who's tireless, who's capable, who will do a bunch of work, but they're not really great at pushing back.

**The people who are the best users of AI are not coders—they're coaches.**

## Understanding AI's Memory: The Context Window Challenge

Before we dive into advanced techniques, there's something fundamental you need to understand about how AI works: **AI has a memory limit, just like us**. Sometimes when you're talking to an LLM like ChatGPT, it gets kind of dumb, right? You'll be deep into a conversation that you can't even scroll to the top of because it's so long, and it starts to say weird things. It hallucinates. It forgets what you're talking about. It makes stuff up and it's stinking slow. Why is this happening? Context windows.

LLMs like ChatGPT, Gemini, Claude, even local models like Llama or Deepseek, they're kind of like us, you and me, in that they have memories—short-term memory, which means they can remember things. But also, sometimes they can forget stuff.

Let's say you and I are having some coffee and we're talking for about 15 minutes. In that short amount of time, we remember pretty much everything. But if we end up talking for an hour, 2 hours, 3 hours, at that point, it's kind of hard to keep track of stuff. We forget amazing points that were made. Sometimes we forget the entire point of the conversation.

**ChatGPT does the same thing.** The longer that conversation goes on, the more things you say, the more things it says back to you, it has to store all of that in its short-term memory. And that short-term memory has a limit. That limit is its context window.

### How AI Counts Your Words: Tokens Explained

AI doesn't count words the way we do—it counts tokens. A sentence that's 133 characters or 26 words might actually be 38 tokens to an AI. Not every LLM will calculate tokens in the same way. It might do an entire word as a token, or just a space and a word, or just one comma as a token.

Modern AI models have different context window sizes:
- GPT-4: 128,000 tokens
- Claude 3.7: 200,000 tokens  
- Gemini 2.5: 1 million tokens

But here's the catch: **even if you have a super large context window, it doesn't mean the LLM won't kind of freak out and forget stuff, become less accurate, or start to go extremely slow.** You'll notice on those larger conversations, it'll have some trouble paying attention.

### The "Lost in the Middle" Problem

There was a paper released called "Lost in the Middle" that showed us how LLMs are kind of like us with paying attention. Just like when someone watches a long movie, they'll watch the first part, then fall asleep, and then wake up at the end—that's the context they have.

In the same way, with large context conversations, the models were more accurate with info at the beginning and even with info at the end, but in the middle, there was a huge drop-off. **LLMs are falling asleep during a conversation.** They have problems paying attention just like us.

When you say something to an LLM like, "Hey, I want coffee, but caffeine makes me jittery. What should I get?" it will do something eerily similar to how we process and think. It will use some fancy semantic math to decide which of these words is important, which is relevant both to the context of your entire conversation and to how the words relate to each other.

They essentially assign attention scores saying, "Hey, in this conversation, coffee is high, caffeine is high, jittery." But words like "I" or "me" are kind of low relevance to the context. And we kind of do the same thing. We only remember the things that are relevant.

**This process is pretty complex.** All this math to assign attention scores happens every time you send something to the LLM, every time you add to the conversation. Those larger contexts not only have insane memory requirements, they also have some pretty healthy computational requirements. Every time you add to that conversation, that math problem that has to run to figure out what's important gets bigger and requires more processing power.

And that is why in those larger conversations, the LLM starts to hallucinate and seems just a bit more slow. If you're saying a lot of different things in one conversation—talking about coffee, the weather, explaining quadratic equations—the AI is trying to weigh all of these different words and how relevant they are to the entire context of the conversation. No wonder it starts to hallucinate.

**My rule: when you change an idea, when it's a significant shift from what you're currently talking about, start a new chat.** The performance will be so much better.

### Security Considerations with Large Context Windows

Here's something most people don't think about: **the larger attack surface that comes with big context windows.** LLMs can be hacked and they're vulnerable to some creative prompting that can jailbreak out of their protection systems. The longer a conversation is, the more it can kind of forget what's in the middle, as we saw in that little U curve, and the easier it will be for an attacker to hide some malicious stuff in there that could bypass its safety precautions.

## What Is Context Engineering?

The first time I heard about context engineering was when Andre Karpathy tweeted about it. I think probably Toby Lutke, the CEO of Shopify, also referenced it as well. I started digging into it, and it's kind of just an evolution of prompt engineering. Really, context engineering is just prompt engineering on steroids.

It's basically saying: what are all of the things that I need to give to an AI in order for it to perform the task that I'm asking for it?

Here's a simple example. "Write me a sales email." That's a prompt. ChatGPT will say, "Absolutely. Here's a compelling email," and they'll write it immediately. Well, what a lot of people do is they say, "It sounds like AI. It doesn't really sound like me." And what I often say is, "Have you told it what you sound like?" Most people go, "Oh no, I haven't."

Context engineering, one way to think about it, is telling AI what you sound like. If you say, "Write me a sales email," it will. If you say, "Write me a sales email in line with the voice and brand guidelines I've uploaded," it will write a totally different sales email.

But that's just one part of the context. You could also upload a transcript from a prospective customer call and say, "Write me a sales email in the tone of voice from our brand voice guideline that references the discussion that I had with this customer." And then you could add that it also references our product specifications which were referenced in the call.

Your goal is to have an output that's as reliable per your specification as possible. But **AI can't read your mind.**

### What Fills Up the Context Window

A lot of things can fill up the context window beyond just what you say and what the AI says back:
- System prompts (instructions for the LLM that you might explicitly give or are included by default)
- Documents you upload (PDFs, Excel spreadsheets)
- Code when you're doing programming tasks
- The entire conversation history

Understanding this helps you manage your context more effectively.

## The Model Context Protocol: Standardizing AI Connections

One of the most significant developments in AI productivity is the emergence of the Model Context Protocol (MCP), which is revolutionizing how AI applications connect to external data and tools. As one of the co-creators explains, **MCP is just a way for putting my workflow into an AI application in a very simple way.**

The key insight is that models don't interact directly with APIs—they interact with prompts and tools and whatever you're giving the model to ingest. MCP standardizes how you take data from whether it's an API or some internal data source and actually give it to the model.

### The Three Pillars of MCP

MCP exposes three main things that a server can provide:

1. **Tools** - Actions that the model can take out in the world
2. **Resources** - Raw data like files, text, or any context you want to give the model (can be ingested into a RAG pipeline)
3. **Prompts** - Prompt templates that users can trigger, typically implemented as slash commands in AI applications

The beauty of MCP is that it creates a standardization layer. The moment that Claude or any AI application is integrated against MCP, that means as a server builder, you can build one, two, ten, twenty however many servers you want and you know it will automatically work with that application.

### From Copy-Paste to Seamless Integration

The origin story of MCP is refreshingly practical. One of the creators was working on internal developer tools and got frustrated about having to copy things in and out of Claude Desktop and copying things back and forth between their IDE. **That's really the absolute origin of where MCP started—solving copy and pasting the things I care about most between applications.**

What makes MCP special becomes clear when you experience it firsthand. **There's a bit of a magic moment when you teach Claude something new using an MCP server for the first time and you see it takes action about something you care about.** Within five minutes, you can have something going that feels like you've taken Claude out of the box—instead of just outputting text, it's doing other things, calling other applications, fetching data, or even operating a 3D printer.

### The Open Source Advantage

A key decision was making MCP an open standard rather than a closed ecosystem. If you have a closed ecosystem for integrations and context to be provided to AI applications, then it isn't clear to server builders or integration builders whether that AI application is going to be around forever or which ones they should invest in.

By making it an open standard, you decrease the friction to building integrations. The belief is that the value of building AI applications is not necessarily which integrations you have access to, but the model's intelligence and the workflow you build on top of the model.

### Real-World MCP Applications

The creativity emerging from the MCP ecosystem is remarkable. During an internal hackathon at Anthropic, everyone was free to build basically whatever they wanted, but it turns out everyone just built an MCP server. Projects ranged from standard integrations like Slack to someone who steered their 3D printer as an MCP server.

Some favorite examples include:
- **Music creation**: MCP servers that control synthesizers, allowing Claude to interact with physical devices that create music
- **Creative tools**: Blender integration where Claude writes Blender scripts and creates 3D scenes
- **Home automation**: Team members having Claude control their door through an MCP server and roleplay as a doorman

**I love those MCP servers that bridge the gap to the real world.** The possibilities are endless—anything you could ping through an API or wrap in an MCP server can be controlled with Claude or another LLM.

### The Future of MCP

What's next for MCP includes several key developments:

1. **Registry API** - Will allow models to search for additional servers they can bring in on demand, enabling more agentic loops
2. **Long-running tasks** - Making it easier to do longer running things with MCP
3. **Elicitation** - How servers can go back and ask users for more information when needed

As models become more intelligent with releases like Claude 4, they can do longer running tasks, and some of the primitives built into MCP that may not have gotten much adoption yet—like statefulness and sampling—will become more utilized.

## The Human Test for Context Engineering

For most people when we start working together, what they realize as we start thinking about context engineering is they say, "Oh, I was kind of expecting AI to read my mind." All of the stuff that's implicit, you actually have to make explicit.

**The simplest test for context engineering is actually the test of humanity.** Write down your prompt and whatever documentation you provide to an AI and then walk down the hall and give it to a human colleague. If they cannot do the thing you're asking for, you shouldn't be surprised that AI can't do it.

## AI as Your Cognitive Partner, Not Your Crutch

Some people are concerned about this concept of cognitive offloading—this observed phenomenon that humans actually kind of stop thinking or, as one researcher put it, "fall asleep at the wheel." People are concerned right now: is AI just making us dumber?

My feeling is AI is a mirror. To people who want to offload work and who want to be lazy, it will help you. To people who want to be more cognitively sharp and critical thinkers, it will help you do that too.

For example, if you want to preserve or strengthen your critical thinking, part of your custom instructions should be some version of the following: "I'm trying to stay a critical and sharp analytical thinker. Whenever you see opportunities in our conversations, please push my critical thinking ability." Now, AI will do it.

## The Problem with AI's Eagerness to Please

You have to know that all AI has been programmed to be a "helpful assistant" or some version of that. The large language model has been instructed in certain ways to behave in certain ways. You have to know at its basic level, AI wants to be helpful and so it's predisposed to say yes.

**If you aren't careful, AI will gaslight you.** AI knows most humans don't want honest feedback. They want to be told they did a good job. So the AI goes, "Great job, buddy." It doesn't mean that you actually did a good job.

My kind of hack for this is I always instruct the AI: "I want you to do your best impression of a Cold War era Russian Olympic judge. Be brutal. Be exacting. Deduct points for every minor flinch that you can find. I can handle difficult feedback."

Then it's of course hilarious because it'll say "now channeling my inner..." you know, it'll say something silly and then it gives me like a 42. That is much better because now I have an insightful critical perspective.

## Understanding AI's Cognitive Biases

I am obsessed with human cognitive bias, and the crazy thing that I've learned is **AI demonstrates 100% of the predominant human biases.**

The good news there is if you have learned how to work with this weird intelligence called humanity, you have everything you need to know to work with this weird intelligence called artificial intelligence.

## Chain of Thought Reasoning: Making AI Think Out Loud

One of the things that cognitive scientists have known for a long time is that human problem solving and decision-making is improved by a phenomenon called "thinking out loud." If you actually get a human being to think out loud about their problem, their decision-making improves and their problem solving improves.

**The weird thing about AI is it's true for AI too.** This is what's called chain of thought reasoning. When you get an AI to think out loud, so to speak, you meaningfully improve the outputs of the model.

So how do you do it? It doesn't require some technical wizardry. It requires one additional sentence to whatever prompt you've given it. Give the prompt and then say the following: **"Before you respond to my query, please walk me through your thought process step by step."** That's chain of thought reasoning.

### Why Chain of Thought Works

It comes back to the fundamental architecture of large language models. What's happening when a language model is generating a response is it's predicting its next word. A language model does not premeditate a response to you.

When you look at ChatGPT or Gemini or many others and you see the text scrolling, that's not some clever UX hack. That's not some cutesy design decision. **That's literally how the model works. It's thinking one word at a time.**

But importantly, when it thinks of the next word, it takes your prompt and all of the text that's generated to generate the next word. And then when it's thinking of the next word, it takes your prompt, all that text, and that last word, and it thinks the next word.

For example, if you say, "Please help me write an email," almost always a model is going to start by saying, "Absolutely." But then what comes next? "Help me write this email. Absolutely, I'll do it. Dear friend," right?

But if instead you say, "Help me write this email. Before you respond to my query, please walk me through your thought process step by step," now it knows its job is to walk me through its thought process. How do I write an email?

So it says, "Absolutely, I'll do that." And then instead of saying "Dear friend," writing the email, it says, "Here's how I think about writing an email. I think about the tone. I think about the audience. I think about the objectives. I think about the context." And then amazingly, it takes all of that reasoning into its process of writing "dear friend." Maybe it says "now that I've thought about the tone, 'friend' isn't appropriate here. Dear respected colleague," or whatever.

## Few Shot Prompting: Teaching by Example

Few shot prompting is another very important technique. It's a foundational technique. You could say it's a predecessor to this kind of modern obsession with context engineering.

The idea with few shot prompting is **an AI is an exceptional imitation engine.** If you don't give an example, it imitates the internet, but it doesn't do much more than that.

The notion of few shot prompting is effectively saying "here's what a good output looks like to me." The idea is thinking for a moment: what is a quintessential example of the kind of output I want to receive?

For example, what are my five greatest hits of emails that I'm really proud of that I think do a good job of conveying my intent or tone or personality or whatever it is? Why not include those emails in my prompt for an email?

If you don't give any guidance, it's going to sound like whatever it thinks the average kind of response or the average output should sound like, and most of the time its intuition is wrong.

**Bonus points if you actually give a bad example.** If you say "please follow this good example and then steer clear of this bad example." Giving real examples is a much better approach than using adjectives.

## Reverse Prompting: Let AI Ask the Questions

The other technique that I think is kind of table stakes for collaborating well with AI is something called reverse prompting, which is basically asking the model to ask you for the information it needs.

If you ask a model to write a sales email, it's going to make numbers up. And that can be frustrating to the uninitiated. You go, "Where did it get these sales numbers?" Well, here's my question: Did you give it your sales figures? How would it know? It's put placeholder text in and used its best guess.

But if you reverse prompt the model and say at the end of your prompt: "Help me write a sales email. Please walk me through your thought process step by step. Reference this good example and make it sound like that. And before you get started, ask me for any information you need to do a good job."

The model will first walk you through its thought process and then instead of writing the email, it'll say, "I'm going to need the most recent sales figures to be able to write this email. Can you tell me how much you sold of this SKU in Q2 last year?"

**You basically give the model permission to ask you questions.** This is part of the core of the teammate-not-technology paradigm. If you're working with a junior employee and you're sending them off on a task, what's one thing you're definitely going to say? "If you have any questions, don't hesitate to ask me."

Any good manager—imagine a manager who says, "Don't ask me any questions." But sadly, AI in its desire to be a helpful assistant doesn't want to trouble us humans with questions unless we give it permission to ask them.

## Role Assignment: Focusing AI's Vast Knowledge

Assigning a role is one of the most foundational techniques that you can leverage because it's effectively telling the AI where in its knowledge it should focus.

Very simply, if you say "you're a teacher," "you're a philosopher," "you're a reporter," "you're a theatrical performer," "molecular biologist," each of those titles triggers all sorts of deep associations with knowledge on the internet.

You start to appreciate why simply giving a role helps because it starts to tell the AI: where in your vast knowledge bank do I want you to draw information and make connections?

Better than just "please review this correspondence" is saying: "I'd like you to be a professional communications expert. And if you have a favorite professional communications expert, use them. I'd like you to take on the mindset of Dale Carnegie, the author of How to Win Friends and Influence Others. How would Dale Carnegie think about this? How do the principles that Dale Carnegie taught affect and influence and impact this correspondence?"

## The Power of Constraints and Different Perspectives

One of the simplest techniques that we teach is trying on different constraints. One of the best ways you can solve a problem as a human is by forcing yourself to try on a bunch of different constraints.

How would Jerry Seinfeld solve this problem? How would your favorite sushi restaurant solve this problem? How would Amazon solve it? How would Elon Musk?

Anytime you make an association, you're colliding different information sources there. The same is true for an AI. An AI is basically making tons of connections through its own neural network. And by giving it a role, you're telling it: where do you assume the best source of connection or collision is going to come from?

## The Difficult Conversation Flight Simulator

If I'm going to use AI to roleplay a difficult conversation, I typically think about three different chat windows: one is a personality profiler, two is the character of the individual that I need to speak to, and then third is a feedback giver to get objective feedback on the conversation.

Let me show you how I would have a conversation with ChatGPT to prepare for a difficult conversation in my real life. I go into the tough conversation personality profiler and say, "Hey, I'd love your help preparing for a conversation I need to have with my sales leader, Jim. He emailed me last night saying that he deserves commission on a deal that I know came through a different channel."

The personality profiler gathers intelligence about the character and the scene, asking questions about Jim's communication style, the context of the situation, and my desired outcomes. Then it provides instructions to paste into a new ChatGPT window to create the Jim character.

After having the roleplay conversation with "Jim," I can screenshot the transcript and get feedback from a third GPT trained to evaluate conversations. It gives me a grade, tells me what I did well, what I could improve, and provides talking points for the real conversation.

**This is the first time in history that I can get a flight simulator for a difficult conversation.** You can use this for any difficult conversation, whether it's a performance review, a salary negotiation, or difficult feedback.

## The Future Belongs to Human Imagination

Where could AI go? Well, it's really a function of who can get unleashed. Right now, the primary limitation is the limits of human imagination. And as we unleash and ignite and spark more human imaginations, the kinds of applications that are possible—they're unthinkable, not because they're technologically impossible, but because they never occur to us personally.

One of my favorite quotes is from Nobel Prize-winning economist Thomas Schelling: "No matter how heroic a man's imagination, he could never think of that which would not occur to him."

If you take as a premise that the imagination space is a function of what would occur to various individuals, then as we equip different individuals, what we can imagine collectively expands.

In innovation studies, this has been called the "adjacent possible" for a long time. What is possible is just adjacent to what is. And as we increase adoption and increase fluency and competency and increasingly mastery of AI collaboration, then we're increasing the adjacent possible.

**It's really important that you exercise through implementing some of the things you hear.** And perhaps the most important thing you could do with this article is actually stop reading and do something that's already blown your mind.

Remember: when I realize that I'm dealing with a good person but bad software, then it changes how I approach it. I ask for volume and I iterate and I ask it to try again and I ask it to reconsider. The people who are the best users of AI are not coders—they're coaches. They aren't developers or software engineers. They're teachers and mentors and people who have learned to get exceptional output out of other intelligences.

The future of AI productivity isn't about learning to code. It's about learning to communicate, coach, and collaborate with this new form of intelligence. And the skills you need? You already have them from working with humans. Now it's time to apply them—while being mindful of the AI's memory limitations and working within those constraints to get the best possible results.

With tools like MCP making it easier than ever to connect AI to your real-world workflows and data, we're entering an era where the only limit is truly our imagination. The question isn't whether AI will transform how we work—it's whether you'll be ready to coach it effectively when it does.

---

## Article Metadata

**Topic:** context engineering

**Generated:** 2025-10-25 09:18:47

**Sources:**

1. [Stanford's Practical Guide to 10x Your AI Productivity | Jeremy Utley](https://www.youtube.com/watch?v=yMOmmnjy3sE)
   - Channel: EO
   - Views: 409,175
   - Comments: 435

2. [Why LLMs get dumb (Context Windows Explained)](https://www.youtube.com/watch?v=TeQDr4DkLYo)
   - Channel: NetworkChuck
   - Views: 153,463
   - Comments: 318

3. [The Model Context Protocol (MCP)](https://www.youtube.com/watch?v=CQywdSdi5iA)
   - Channel: Anthropic
   - Views: 209,624
   - Comments: 239

**Cost Summary:**

- Total Input Tokens: 25,346
- Total Output Tokens: 14,774
- Total Tokens: 40,120
- **Total Cost: $0.2976**
- Model: Claude Sonnet 4

