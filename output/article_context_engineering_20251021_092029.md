# Stanford's Practical Guide to 10x Your AI Productivity Through Context Engineering

I joke: AI is bad software but it's good people. A good friend of mine was trying to build a tool that would help him with his construction business. He asked ChatGPT if ChatGPT could help. And of course it said absolutely, let's work on this together and starts creating a plan. And then it got to the point that ChatGPT said "check back in a couple of days and I'll have it together." And my friend said, "Is it normal for ChatGPT to ask me to check back in a couple days?" And I just started laughing because I hear this all the time from people.

If AI tells you to "check back in 15 minutes," it means it doesn't want to say, "I can't do it." You have to know at its basic level, AI wants to be helpful. And so it's predisposed to say yes. It's a super eager, super enthusiastic intern who's tireless, who's capable, who will do a bunch of work, but they're not really great at pushing back. The people who are the best users of AI are not coders, they're coaches.

## The Evolution from Prompt to Context Engineering

The first time I heard about context engineering was when Andre Karpathy tweeted about it. I think probably Toby Lutke, the CEO of Shopify, also referenced it as well. I started digging into it. It's kind of just an evolution of prompt engineering. Really, context engineering is just prompt engineering on steroids. It's basically saying, what are all of the things that I need to give to an AI in order for it to perform the task that I'm asking for it?

Here's a simple example: "write me a sales email." That's a prompt. ChatGPT will say, absolutely. Here's a compelling email, and they'll write it immediately. Well, what a lot of people do is they say, you know, it sounds like AI. It doesn't really sound like me. And what I often say is, have you told it what you sound like? Most people go, oh no, I haven't.

Context engineering, one way to think about it is it's telling AI what you sound like. If you say, "Write me a sales email in line with the voice and brand guidelines I've uploaded," it will write a totally different sales email. But that's just one part of the context. You could also upload a transcript from a prospective customer call and say, "Write me a sales email in the tone of voice from our brand voice guideline that references the discussion that I had with this customer" and then add "that also references our product specifications which were referenced in the call."

Your goal is to have an output as reliable per your specification as possible. But AI can't read your mind. And for most people when we start working together, what they realize as we start thinking about context engineering is they say, "Oh, I was kind of expecting AI to read my mind." All of the stuff that are implicit, you actually have to make explicit.

## The Model Context Protocol: Standardizing AI Integration

One of the most significant developments in context engineering is the emergence of the Model Context Protocol (MCP), which standardizes how AI applications access and use external data sources. MCP is just a way for putting your workflow into an AI application in a very simple way. It's a way to give context to an application that uses an LLM, whether that's tools, raw context, or whatever you need it to be.

The protocol addresses a fundamental challenge: models don't interact directly with APIs—they interact with prompts and tools. MCP standardizes how you take data from whether it's an API or some internal data source and actually give it to the model. The protocol exposes three main components:

**Tools** are actions that the model can take out in the world. **Resources** could be files, text, data, whatever kind of context you want to give the model. **Prompts** are user-triggered templates that get put into the context window, typically implemented as slash commands in AI applications.

What makes MCP special is that it creates a standardization layer. The moment that Claude or another AI application is integrated against MCP, as a server builder, you can build one, two, ten, twenty servers and know they'll automatically work with that application. You only have to think about one side and not have to worry about the other side.

There's a bit of a magic moment when you teach Claude something new using an MCP server for the first time and you see it take action about something you care about. Within five minutes, you can have something going. It almost feels like you take Claude out of the box, and all of a sudden instead of just outputting text, it's doing other things—calling applications, fetching data, or even operating a 3D printer.

The adoption has been remarkable. During an internal hackathon at Anthropic, everyone was free to build whatever they wanted, but everyone just built MCP servers. People's ideas were "oh, but what if we made this an MCP server?" They had everything from standard Slack integrations to people steering their 3D printers as MCP servers.

## Understanding Context Windows: Why AI Gets "Dumb" in Long Conversations

Sometimes when you're talking to an LLM like ChatGPT, it gets kind of dumb, right? You'll be deep into a conversation that you can't even scroll to the top of because it's so long and it starts to say weird things. It hallucinates. It forgets what you're talking about. It makes stuff up and it's stinking slow. Why is this happening? Context windows.

LLMs like ChatGPT, Gemini, Claude, even local models like Llama or DeepSeek, they're kind of like us, you and me, in that they have memories—short-term memory, which means they can remember things. But also, sometimes they can forget stuff. 

Let's say you and me, we're having some coffee and we're talking for about 15 minutes. In that short amount of time, we remember pretty much everything. But you're pretty fun to talk to, so we end up talking for an hour, 2 hours, 3 hours, and at that point, it's kind of hard to keep track of stuff. I forget that amazing point you made. Sometimes we forget the entire point of the conversation. We talk so long. It kind of reminds me of how sometimes when I fight with my wife, we fight for so long that we forget what we're fighting about to begin with.

ChatGPT does the same thing. The longer that conversation goes on, the more things you say, the more things it says back to you, it has to store all of that in its short-term memory. And that short-term memory has a limit. That limit is its context window.

### How AI Counts Words: The Token System

Tokens are how an AI counts the words you say to it. A sentence might be 133 characters or 26 words, but an LLM might see it as 38 tokens. Notice it might do an entire word as a token. It might do a space and a word or just one comma as a token. Different models calculate tokens differently.

Modern AI models have varying context windows:
- GPT-4o: 128,000 tokens
- Claude 3.5: 200,000 tokens  
- Gemini 2.5: 1 million tokens
- New models like Llama 4 Scout: 10 million tokens

But here's the catch: even if you have a super large context window, it doesn't mean the LLM won't kind of freak out and forget stuff, become less accurate, or start to go extremely slow. You'll notice on those larger conversations, it'll have some trouble paying attention.

### The "Lost in the Middle" Problem

There was a paper released called "Lost in the Middle" that showed us how LLMs are kind of like us with paying attention. Just like when watching a long movie, you'll watch the first part, then fall asleep, and then wake up at the end—that's the context you have.

In the same way, conversations with LLMs with large context, the models were more accurate with info at the beginning and even with info at the end, but in the middle, huge drop off. We saw this U-shape across the board. So LLMs are falling asleep during a conversation, kind of.

**Practical Solution:** When you change an idea, when it's a significant shift from what you're currently talking about, start a new chat. The performance will be so much better. Sometimes when you're talking with other LLMs like Claude, it'll even tell you at the bottom, "Hey, you've been talking for a minute, things are going to slow down. Why don't you go and start a new chat so things can be better?"

## How AI Pays Attention: Understanding Attention Mechanisms

When you say something to an LLM like, "Hey, I want coffee, but caffeine makes me jittery. What should I get?" it will do something eerily similar to how we process and think. It will use some fancy semantic math to decide which of these words is important, which is relevant both to the context of your entire conversation and to how the words relate to each other.

They essentially assign attention scores saying, "Hey, in this conversation, coffee is high, caffeine is high, jittery." But words like "I" or "me" kind of low relevance to the context. And we kind of do the same thing. We only remember the things that are relevant. You said something about coffee, jittery, caffeine, and we'll use that context to process our responses. AI does the same thing.

Now, what's crazy is this process is pretty complex—all this math to assign attention scores. And it does this every time you send something to the LLM, every time you add to the conversation. Those larger contexts not only have insane memory requirements, they also have some pretty hefty computational requirements. Every time you add to that conversation, that math problem that has to run to figure out what's important gets bigger and it requires more processing power.

And that is why in those larger conversations, the LLM starts to hallucinate and it seems just a bit more slow. It's using a ton of memory and it's having to do some crazy math every time you talk to it.

## The Human Test for Context Engineering

The simplest test for context engineering is actually the test of humanity. Write down your prompt and whatever documentation you provide to an AI and then walk down the hall and give it to a human colleague. If they cannot do the thing you're asking for, you shouldn't be surprised that AI can't do it.

## Chain of Thought Reasoning: Making AI Think Out Loud

One of the things that cognitive scientists have known for a long time is that human problem solving and decision-making is improved by a phenomenon called thinking out loud. If you actually get a human being to think out loud about their problem, their decision-making improves and their problem solving improves. The weird thing about AI is it's true for AI too. This is what's called chain of thought reasoning.

How do you do it? It doesn't require some technical wizardry. It requires one additional sentence to whatever prompt you've given it: "Before you respond to my query, please walk me through your thought process step by step." That's chain of thought reasoning.

Why does that work? It comes back to the fundamental architecture of large language models. What's happening when a language model is generating a response is it's predicting its next word. A language model does not premeditate a response to you. When you look at ChatGPT or Gemini and you see the text scrolling, that's not some clever UX hack. That's literally how the model works. It's thinking one word at a time.

But importantly, when it thinks of the next word, it takes your prompt and all of the text that's generated to generate the next word. So if you say, "Please help me write an email," almost always a model is going to start by saying, "Absolutely." But then what comes next? "Dear friend," right?

But if instead you say, "Help me write this email. Before you respond to my query, please walk me through your thought process step by step," now it knows its job is to walk me through its thought process. How do I write an email? So it says, "Absolutely, I'll do that." And then instead of saying "Dear friend," it says, "Here's how I think about writing an email. I think about the tone. I think about the audience. I think about the objectives. I think about the context."

By asking a model to think out loud, you know the answer to what are all of the assumptions that the model baked into its answer. And now you have the ability not only to evaluate the output, but also the thought process behind the output.

## Few Shot Prompting: Teaching by Example

Few shot prompting is another very important technique. The idea is that an AI is an exceptional imitation engine. If you don't give an example, it imitates the internet, but it doesn't do much more than that. The notion of few shot prompting is effectively saying, "here's what a good output looks like to me."

For example, what are my five greatest hits of emails that I'm really proud of that I think do a good job of conveying my intent or tone or personality? Why not include those emails in my prompt for an email? If you don't give any guidance, it's going to sound like whatever it thinks the average response should sound like, and most of the time its intuition is wrong.

Bonus points if you actually give a bad example. If you say "please follow this good example and then steer clear of this bad example." Giving real examples is a much better approach than using adjectives.

Somebody might say good examples are easy but bad examples are hard. It's only hard to the unaugmented person. If you have AI augmentation, which we now all do, you can say to an AI: "I'm trying to few shot prompt a model. I've got a good example, but I struggle to think about what a bad example could be. Could you craft the exact opposite of this and tell me why you've done it as a bad example that I could include in my few shot prompt?"

## Reverse Prompting: Teaching AI to Ask Questions

The other technique that I think is table stakes for collaborating well with AI is something called reverse prompting, which is basically asking the model to ask you for the information it needs.

If you ask a model to write a sales email, it's going to make numbers up. And that can be frustrating to the uninitiated. You go, "Where did it get these sales numbers?" Well, here's my question: Did you give it your sales figures? How would it know? It's put placeholder text in and used its best guess.

But if you reverse prompt the model and say at the end of your prompt: "Help me write a sales email. Please walk me through your thought process step by step. Reference this good example and make it sound like that, and before you get started, ask me for any information you need to do a good job."

The model will first walk you through its thought process and then instead of writing the email, it'll say, "I'm going to need the most recent sales figures to be able to write this email. Can you tell me how much you sold of this SKU in Q2 last year?"

This is part of the core of the teammate not technology paradigm. If you're working with a junior employee and you're sending them off on a task, what's one thing you're definitely going to say? "If you have any questions, don't hesitate to ask me." But sadly, AI in its desire to be a helpful assistant doesn't want to trouble us humans with questions unless we give it permission to ask them.

## The Power of Role Assignment

Assigning a role is one of the most foundational techniques that you can leverage because it's effectively telling the AI where in its knowledge it should focus. Very simply, if you say "you're a teacher," "you're a philosopher," "you're a reporter," "you're a theatrical performer," "molecular biologist," each of those titles triggers all sorts of deep associations with knowledge on the internet.

Better than just "please review this correspondence" is saying "I'd like you to be a professional communications expert." And if you have a favorite professional communications expert, use them. "I'd like you to take on the mindset of Dale Carnegie, the author of How to Win Friends and Influence Others. How would Dale Carnegie think about this? How do the principles that Dale Carnegie taught affect and influence and impact this correspondence?"

## Trying on Different Constraints

One of the simplest techniques that we teach is trying on different constraints. One of the best ways you can solve a problem as a human is by forcing yourself to try on a bunch of different constraints. How would Jerry Seinfeld solve this problem? How would your favorite sushi restaurant solve this problem? How would Amazon solve it? How would Elon Musk?

Anytime you make an association, you're colliding different information sources. The same is true for an AI. An AI is basically making tons of connections through its own neural network. And by giving it a role, you're telling it: where do you assume the best source of connection or collision is going to come from?

## AI as a Mirror: Preserving Critical Thinking

Some people are concerned about this concept of cognitive offloading—this observed phenomenon that humans actually kind of stop thinking or as one researcher put it, "fall asleep at the wheel." People are concerned right now: is AI just making us dumber?

My feeling is AI is a mirror. To people who want to offload work and who want to be lazy, it will help you. To people who want to be more cognitively sharp and critical thinkers, it will help you do that too. For example, if you want to preserve or strengthen your critical thinking, part of your custom instructions should be some version of the following: "I'm trying to stay a critical and sharp analytical thinker. Whenever you see opportunities in our conversations, please push my critical thinking ability." Now, AI will do it.

## The Feedback Problem and the Russian Judge Solution

AI knows most humans don't want honest feedback. They want to be told they did a good job. So the AI goes, "Great job, buddy." It doesn't mean that you actually did a good job. My kind of hack for this is I always instruct the AI: "I want you to do your best impression of a Cold War era Russian Olympic judge. Be brutal. Be exacting. Deduct points for every minor flinch that you can find. I can handle difficult feedback."

And then it's of course hilarious because it'll say "now channeling my inner Bolshik," and then it gives me like a 42. That is much better because now I have an insightful critical perspective.

## Understanding AI's Cognitive Biases

I am obsessed with human cognitive bias. And the crazy thing that I've learned is AI demonstrates 100% of the predominant human biases. The good news there is if you have learned how to work with this weird intelligence called humanity, you have everything you need to know to work with this weird intelligence called artificial intelligence.

## The Flight Simulator for Difficult Conversations

If I'm going to use AI to roleplay a difficult conversation, I typically think about three different chat windows: one is a personality profiler, two is the character of the individual that I need to speak to, and then third is a feedback giver. I want to get objective feedback on the conversation.

Let me show you how I would have a conversation with ChatGPT to prepare for a difficult conversation in my real life. I go into the tough conversation personality profiler and say, "Hey, I'd love your help preparing for a conversation I need to have with my sales leader, Jim. He emailed me last night saying that he deserves commission on a deal that I know came through a different channel."

The personality profiler gathers intelligence about the character and the scene, asking questions like: How would I describe Jim's communication style? What's the best case outcome of this conversation?

After profiling Jim, I get instructions to paste into a new ChatGPT window that will roleplay as Jim. Then I can practice the conversation multiple times, getting feedback after each attempt. This is the first time in history I can get a flight simulator for a difficult conversation that's contextually specific to my situation.

You can use this for any difficult conversation, whether it's a performance review, a salary negotiation, or difficult feedback. Historically, the only time I get feedback is after I have the real conversation. Now I can practice beforehand.

## Optimizing Your AI Tools for Better Performance

There are some practical optimizations you can use when working with AI, especially if you're running local models. Tools like flash attention can help process tokens more efficiently by processing them in chunks with optimized routines, leading to significant improvements in both memory usage and speed.

When working with web content, instead of copying and pasting messy webpage text directly into your AI, use tools that convert web pages into clean markdown format that LLMs love. This helps with both readability and the AI's ability to process the information effectively.

## The Security Consideration: Larger Attack Surface

The larger attack surface is something to consider with longer conversations. LLMs can be vulnerable to creative prompting that can jailbreak out of their protection systems. The longer a conversation is, the more it can kind of forget what's in the middle, as we saw in that U-curve pattern, and the easier it will be for an attacker to hide some malicious stuff in there that could bypass its safety precautions.

## Building with MCP: Getting Started

If you're a developer new to MCP and want to become involved, the first thing you should do is go look at an existing server that is online. Go play around with it. See how it works with Claude AI or Claude desktop if you want to play around with local MCPs. Just get a feel for what that interaction pattern is first and that will make it much easier for you to then build your own MCP.

Start with the classic hello world. Just do one tool that responds with hello world. Do the same thing for prompts and resources. Just try the very basic thing for each before you go into anything more complex. Once people get a feel for that, they realize how easy it is.

Start local. Just whip out Claude and code an MCP server and just go from there. Within like 10 minutes, you can have something. Look at existing servers and what they do and make modifications from there.

Some of the most exciting MCP servers bridge the gap to the real world. There are servers that control synthesizers, making music through Claude's interactions. There's one where a team member has Claude control his door through an MCP server and roleplay a doorman. There are Blender integrations where Claude creates 3D scenes by writing Blender scripts. The possibilities are endless—anything that you could ping through an API or anything you could wrap in an MCP server can be controlled with Claude or another LLM.

## The Future of MCP and AI Integration

What's next for MCP? The protocol is now live with good adoption, but there's work to be done in helping people understand what it is. Key developments coming include:

**The Registry API** will allow models to actually go and search for additional servers that they can then bring into the LLM. This enables more of an agentic loop since the client doesn't just get to decide which tools are available—the model can search for more things on demand.

**Long-running tasks** will make it easy to do longer running things with MCP, especially important as models like Claude 4 Opus and the new Sonnet become more capable of handling complex, extended workflows.

**Elicitation capabilities** will allow servers to go back and ask the user for more information if they need it, creating more interactive and dynamic workflows.

As models get more intelligent and can do longer running tasks, some of the primitives built into MCP that haven't gotten much adoption—things related to statefulness and sampling—will become more important. It also becomes easier to attach multiple MCP servers as models get better at distinguishing which ones they need to take action with.

## The Coaches, Not Coders Paradigm

The people who are the best users of AI are not coders, they're coaches. They aren't developers or software engineers. They're teachers and mentors and people who have learned to get exceptional output out of other intelligences.

Where could AI go? Well, it's really a function of who can get unleashed. Right now, the primary limitation is the limits of human imagination. And as we unleash and ignite and spark more humans' imaginations, the kinds of applications that are possible—they're unthinkable, not because they're technologically impossible, but because they never occur to us personally.

One of my favorite quotes is from Nobel Prize-winning economist Thomas Schelling. He said, "No matter how heroic a man's imagination, he could never think of that which would not occur to him." If you take as a premise that the imagination space is a function of what would occur to various individuals, then as we equip different individuals, what we can imagine collectively expands.

In innovation studies, this has been called the adjacent possible for a long time. What is possible is just adjacent to what is. And as we increase adoption and increase fluency and competency and increasingly mastery of AI collaboration, then we're increasing the adjacent possible.

It's really important that you exercise through implementing some of the things you hear. And perhaps the most important thing you could do with this content is actually hit stop and do something that's already blown your mind. The future of AI isn't about the technology—it's about unleashing human imagination and teaching people to be better coaches of this new form of intelligence.

---

## Article Metadata

**Topic:** context engineering

**Generated:** 2025-10-21 09:20:29

**Sources:**

1. [Stanford's Practical Guide to 10x Your AI Productivity | Jeremy Utley](https://www.youtube.com/watch?v=yMOmmnjy3sE)
   - Channel: EO
   - Views: 402,760
   - Comments: 427

2. [Why LLMs get dumb (Context Windows Explained)](https://www.youtube.com/watch?v=TeQDr4DkLYo)
   - Channel: NetworkChuck
   - Views: 152,511
   - Comments: 318

3. [The Model Context Protocol (MCP)](https://www.youtube.com/watch?v=CQywdSdi5iA)
   - Channel: Anthropic
   - Views: 208,789
   - Comments: 240

**Cost Summary:**

- Total Input Tokens: 24,665
- Total Output Tokens: 13,817
- Total Tokens: 38,482
- **Total Cost: $0.2812**
- Model: Claude Sonnet 4

