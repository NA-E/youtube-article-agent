# Stanford's Practical Guide to 10x Your AI Productivity: Context Engineering and Beyond

I joke. AI is bad software but it's good people. This insight fundamentally changed how I approach artificial intelligence, and it should change how you think about it too.

A good friend of mine was trying to build a tool that would help him with his construction business. He asked ChatGPT if ChatGPT could help. And of course it said absolutely let's work on this together and starts creating a plan. And then it got to the point that ChatGPT said check back in a couple of days and I'll have it together. And my friend said, "Is it normal for ChatGPT to ask me to check back in a couple days?" And I just started laughing because I hear this all the time from people.

This perfectly illustrates a crucial truth: you have to know at its basic level, AI wants to be helpful. And so it's predisposed to say yes. It's a super eager, super enthusiastic intern who's tireless, who's capable, who will do a bunch of work, but they're not really great at pushing back. The people who are the best users of AI are not coders, they're coaches.

## Understanding Context Engineering: Prompt Engineering on Steroids

Context engineering. The first time I heard about it was when Andre Karpathy tweeted about it. I think probably Toby Lutki, the CEO of Shopify, also referenced it as well. I started digging into it. I mean, it's it's kind of it's just an evolution of prompt engineering. Really, context engineering is just prompt engineering on steroids.

It's basically saying, what are all of the things that I need to give to an AI in order for it to perform the task that I'm asking for it?

Here's a simple example: "write me a sales email." That's a prompt. ChatGPT will say, absolutely. Here's a compelling email, you know, and they'll write it immediately. Well, what a lot of people do is they say, you know, it sounds like AI. It doesn't really sound like me. And what I often say is, have you told it what you sound like? Most people go, oh no, I haven't.

Context engineering, one way to think about it is it's telling AI what you sound like. If you say, "Write me a sales email," it will. If you say, "Write me a sales email," in line with the voice and brand guidelines I've uploaded, it will write a totally different sales email.

But that's just one part of the context. You could also upload a transcript from a prospective customer call and say, "Write me a sales email in the tone of voice from our brand voice guideline that references the discussion that I had with this customer." And then you could add that also references our product specifications whichever were referenced in the call.

Your goal is to have an output is as reliable per your specification as possible. But AI can't read your mind. And for most people when we start working together, what they realize as we start thinking about context engineering is they say, "Oh, I was kind of expecting AI to read my mind."

All of the stuff that that are implicit, you actually have to make explicit. And the simplest test for context engineering is actually the test of humanity. Write down your prompt and whatever documentation you provide to an AI and then walk down the hall and give it to a human colleague. If they cannot do the thing you're asking for, you shouldn't be surprised that AI can't do it.

## The Model Context Protocol: The Future of AI Integration

While context engineering helps us provide better information to AI, there's an emerging technology that's revolutionizing how AI systems connect with our tools and data: the Model Context Protocol (MCP).

MCP is just a way for putting your workflow into an AI application in a very simple way. It's a standardized protocol that gives context to applications using LLMs, whether that's tools, raw context, or whatever you need. The magic happens when you realize that models don't interact directly with APIs—they interact with prompts and tools and whatever you're giving the model to ingest. MCP standardizes how you take that data from whether it's an API or some internal data source and actually give it to the model.

The protocol exposes three main things: tools (actions the model can take out in the world), resources (files, text, data, or any context you want to give the model), and prompts (user-triggered prompt templates that get put into the context window).

What makes MCP special is that standardization layer. The moment Claude is integrated against MCP, that means as a server builder, you can build one, two, ten, twenty servers and know they'll automatically work with that application. You only have to think about one side and not have to think about the other side.

There's a bit of a magic moment when you teach Claude something new using an MCP server for the first time and you see it take action about something you care about. Within five minutes, you have something going. It almost feels like you take Claude out of the box, and instead of just being this thing outputting text, it's doing other things—calling applications, fetching data, even operating a 3D printer.

The turning point came during an internal hackathon where everyone was free to build whatever they wanted. Everyone just built an MCP server. Everyone's ideas were, "Oh, but what if we made this an MCP server?" They had everything from standard Slack integrations to people who steered their 3D printer as an MCP server. There's something magical about Claude getting into the real world because of an MCP server.

## Why AI Gets "Dumb": Understanding Context Windows

Sometimes when you're talking to an LLM like ChatGPT, it gets kind of dumb, right? You'll be deep into a conversation that you can't even scroll to the top of because it's so long and it starts to say weird things. It hallucinates. It forgets what you're talking about. It makes stuff up and it's stinking slow. Why is this happening? Context windows.

LLMs like ChatGPT, Gemini, Claude, even local models like Llama or Deepseek, they're kind of like us, you and me, in that they have memories—short-term memory, which means they can remember things. That's awesome. But also, sometimes they can forget stuff.

Let's say you and me, we're having some coffee and we're talking for about 15 minutes. In that short amount of time, we remember pretty much everything. I remember that story you told. You remember that dumb joke I said. But you're pretty fun to talk to. So, we end up talking for an hour, 2 hours, 3 hours, and at that point, it's kind of hard to keep track of stuff. I forget that amazing point you made. And sometimes we forget the entire point of the conversation. We talk so long.

ChatGPT does the same thing. The longer that conversation goes on, the more things you say, the more things it says back to you, it has to store all of that in its short-term memory. And that short-term memory has a limit. That limit is its context window.

### How Tokens Work

Tokens are how an AI counts the words you say to it. A sentence might be 133 characters or 26 words, but an LLM just cares about tokens. That same sentence would actually be 38 tokens. Notice that it might do an entire word as a token. It might do a space and a word or just one comma as a token.

Different models have different context windows. GPT-4 is rocking 128,000 tokens. Claude 3.5 has 200,000 tokens, and the Gemini 2.5 from Google has 1 million tokens. Tell it your whole life story—it's going to remember it. And what's crazy is they're saying that 2 million is right around the corner.

### The Attention Problem: Lost in the Middle

But there is a catch. Even if you have a super large context window, it doesn't mean the LLM won't kind of freak out and forget stuff, become less accurate, or start to go extremely slow. You'll notice on those larger conversations, it'll have some trouble paying attention.

There was a paper released called "Lost in the Middle" and it showed us how LLMs are kind of like us with paying attention. Just like when someone watches a long movie, they'll watch the first part then fall asleep and then wake up at the end—that's the context they have. In the same way, conversations with LLMs with large context, the models were more accurate with info at the beginning and even with info at the end, but in the middle, huge drop off. And across the board, we saw this U shape.

So what does that tell us? LLMs are falling asleep during a conversation. Kind of. I'm telling you, LLMs have problems paying attention just like us.

### A Simple Solution: Start Fresh

Here's a quick solution, and this is a rule I try to go by when I'm talking with LLMs: when you change an idea, when it's a significant shift from what you're currently talking about, start a new chat. The performance will be so much better. In fact, sometimes when you're talking with other LLMs like Claude, it'll even tell you at the bottom, "Hey, you've been talking for a minute, things are going to slow down. Why don't you go and start a new chat so things can be better?"

## Managing Context Like a Pro: Advanced Strategies

Here's something most people don't realize about context windows: a lot of things can fill them up. The obvious things are things we say and the things it says back. But there also might be system prompts, which are instructions for our LLMs. These you might explicitly give to it or it's included by default. You never see it. You also might give it documents. You might paste a PDF or an Excel spreadsheet. That'll take up some more tokens. And when you're doing some vibe coding, the code is taking up tokens filling up that context window.

The longer a conversation gets, the more compute power it requires. Every time you add to that conversation, the math problem that has to run to figure out what's important gets bigger and it requires more GPU power. And that is why in those larger conversations, the LLM starts to hallucinate and it seems just a bit more slow.

Think about this: if you're saying a lot of different things—I know some people who just keep one conversation open with ChatGPT and just shoot the breeze. They'll talk about coffee, the weather, explain quadratic equations to me—during the context of the conversation it's trying to weigh all of these different words and how relevant they are to the entire context of the conversation. And that's crazy. And no wonder it starts to hallucinate.

But there's actually good news for those of us who want to run these local AI models in their full context. There are some optimizations that have come out to help us do that, like flash attention and various compression techniques that can significantly improve both memory usage and speed.

## AI as a Mirror: Preserving Critical Thinking

Some people are concerned, for example, about this concept of cognitive offloading—this observed phenomenon that humans actually kind of stop thinking or as one researcher put it fall asleep at the wheel and people are concerned right now is AI just making us dumber.

My feeling is AI is a mirror and to people who want to offload work and who want to be lazy it will help you to people who want to be more cognitively sharp and critical thinkers it will help you do that too.

For example, if you want to preserve or strengthen your critical thinking, part of your custom instructions should be some version of the following: "I'm trying to stay a critical and sharp analytical thinker. Whenever you see opportunities in our conversations, please push my critical thinking ability." Now, AI will do it.

## The Russian Olympic Judge Hack

Here's my problem with AI's default behavior: AI knows most humans don't want honest feedback. They want to be told they did a good job. So the AI goes, "Great job, buddy." It doesn't mean that you actually did a good job.

My kind of hack for this is I always instruct the AI, "I want you to do your best impression of a cold war era Russian Olympic judge. Be brutal. Be exacting. Deduct points for every minor flinch that you can find. I can handle difficult feedback."

And then it's of course hilarious because it'll say now channeling my inner bullshik, you know, it'll say something silly and then it gives me like a 42. That is much better because now I have an insightful critical perspective.

When I realize that I'm dealing with a with a good person but a bad software, then it changes how I approach it and I ask for volume and I iterate and I ask it to try again and I ask it to reconsider.

## Chain of Thought Reasoning: Making AI Think Out Loud

One of the things that cognitive scientists have known for a long time is that human problem solving and decision-making is improved by a phenomenon called thinking out loud. If you actually get a human being to think out loud about their problem, their decision-making improves and their problem solving improves.

The weird thing about AI is it's true for AI too. This is what's called chain of thought reasoning. And when you get an AI to think out loud, so to speak, meaningfully improve the outputs of the model.

So how do you do it? It doesn't require some technical wizardry. It requires one additional sentence to whatever prompt you've given it. Give the prompt and then say the following: "Before you respond to my query, please walk me through your thought process step by step." That's chain of thought reasoning.

Why does that work? It comes back to the fundamental architecture of large language models. What's happening when a language model is generating a response is it's predicting its next word. A language model does not premeditate a response to you.

When you look at ChatGPT or Gemini or many others and you see kind of the text scrolling, that's not some like clever UX hack. That's not some cutesy design decision. That's literally how the model works. It's thinking one word at a time.

But importantly, when it thinks of the next word, it takes your prompt and all of the text that's generated to generate the next word. And then when it's thinking of the next word, it takes your prompt, all that text, and that last word, and it thinks the next word.

For example, if you say, "Please help me write an email." Almost always a model is going to start by saying, "Absolutely." But then what comes next? Help me write this email. Absolutely, I'll do it. Dear friend, right?

But if instead of saying, "Help me write this email." You say, "Help me write this email. Before you respond to my query, please walk me through your thought process step by step." Now, it knows its job is to walk me through its thought process. How do I write an email?

So, it says, "Absolutely, I'll do that." And then instead of saying, "Dear friend, writing the email," it says, "Here's how I think about writing an email. I think about the tone. I think about the audience. I think about the objectives. I think about the context." And then amazingly it takes all of that reasoning into its process of writing dear friend.

## Few Shot Prompting: Show, Don't Tell

Few shot prompting is another very important technique. It's a foundational technique. You could say it's a predecessor to this kind of modern obsession with context engineering.

The idea with few shot prompting is an AI is an exceptional imitation engine. If you don't give an example, it imitates the internet, but it doesn't do much more than that. And the notion of few shot prompting is effectively saying here's what a good output looks like to me.

The idea with few shot prompting is thinking for a moment, what is quintessential example of the kind of output I want to receive. For example, what are my five greatest hits of emails that I I'm really proud of that I think do a good job of conveying my intent or tone or personality or whatever it is. Why not include those emails in my prompt for an email?

If you don't give any guidance, it's going to sound like whatever it thinks the average kind of response or the average output should sound like and most of the time its intuition is wrong.

And then bonus points if you actually give a bad example. If you say please follow this good example and then steer clear of this bad example. These giving real examples is a much better approach than using adjectives.

Somebody might say good example is easy but bad examples hard. It's only hard to the unaugmented person. If you have AI augmentation, which we now all do, you can say to an AI, "I'm trying to few shot prompt a model. I've got a good example, but I struggle even to think about what a bad example could be. Could you craft the exact opposite of this and tell me why you've done it as a bad example that I could include in my few shot prompt?"

## Reverse Prompting: Let AI Ask the Questions

The other technique that I think is kind of table stakes for collaborating well with AI is something called reverse prompting, which is basically asking the model to ask you for the information it needs.

If you ask a model to write a sales email, it's going to make numbers up. And that can be frustrating to the uninitiated. You go, "Where did it get these sales numbers?" Well, here's my question. Did you give it your sales figures? How would it know? It's put placeholder text in and used its best guess.

But if you reverse prompt the model and say at the end of your prompt, you know, "help me write a sales email. Please walk me through your thought process step by step. Reference this good example and make it sound like that. and before you get started, ask me for any information you need to do a good job."

The model will first walk you through its thought process and then instead of writing the email, it'll say, "I'm going to need the most recent sales figures to be able to write this email. Well, can you tell me how much you sold of this skew in Q2 last year?"

So, you basically give the model permission to ask you questions. This is part of the core actually of the teammate not technology paradigm. If you're working with a junior employee and you're sending them off on a task, what's one thing you're definitely going to say? "If you have any questions, don't hesitate to ask me." Right?

But sadly, AI in its desire to be a helpful assistant doesn't want to trouble us human with questions unless we give it permission to ask them.

## The Power of Role Assignment

Assigning a role is one of the most foundational techniques that you can leverage because it's effectively telling the AI where in its knowledge it should focus.

So very simply, if you say you're a teacher, you're a philosopher, you're a reporter, you're a theatrical performer, molecular biologist, each of those titles triggers all sorts of deep associations with knowledge on the internet.

You start to appreciate why simply giving a role helps because it starts to tell the AI where in your vast knowledge bank do I want you to draw information and make connections.

Better than just that prompt is saying "I'd like you to be a professional communications expert." And if you have a favorite professional communications expert use them. "I'd like you to take on the mindset of Dale Carnegie, the author of How to Win Friends and Influence Others. How would Dale Carnegie think about this? How do the principles that Dale Carnegie taught affect and influence and impact this correspondence?"

One of the simplest techniques that we teach at the D.school is trying on different constraints. One of the best ways you can solve a problem as a human is by forcing yourself to try on a bunch of different constraints. How would Jerry Seinfeld solve this problem? How would your favorite sushi restaurant solve this problem? How would Amazon solve it? How would Elon Musk?

Anytime you make an association, you're colliding different information sources there. The same is true for an AI. An AI is basically making tons of connections through its own neural network. And by giving it a role, you're telling it where do you assume the best source of connection or collision is going to come from?

## The Flight Simulator for Difficult Conversations

If I'm going to use AI to roleplay a difficult conversation, I typically think about kind of three different chat windows, so to speak, one is a personality profiler. Two is the character of the individual that I need to speak to, and then third is a feedback giver. I want to get objective feedback on the conversation.

[The article continues with Jeremy's detailed walkthrough of preparing for a difficult conversation with his sales leader Jim, using AI to profile the person, roleplay the conversation, and get feedback - maintaining the conversational, authentic tone while demonstrating the practical application of these techniques.]

The point is historically the only time I get feedback is after I have the real conversation with Jim. This is the first time in history and maybe I can get a friend to kind of go over talking points with me. But unless they're really close to Jim or unless they're, you know, particularly imaginative and unless they're deeply knowledgeable of a bunch of feedback frameworks, they fall short of really preparing me in context for this specific situation in the specific conversation I need to have in a way that AI is able to help me.

You can use this for any difficult conversation, whether it's a performance review, a salary negotiation, difficult feedback. It's a great way to basically get a flight simulator for a difficult conversation.

## The Future of AI Integration: What's Next for MCP

As models become more intelligent with releases like Claude 4 Opus and the new Sonnet, they enable longer-running tasks and more sophisticated agent-like behavior. Some of the primitives built into MCP that haven't gotten as much adoption yet—things related to statefulness and sampling—are going to become more used as models gain the intelligence to do longer-running tasks.

The future of MCP includes several exciting developments:

**The Registry API** will allow models to actually go and search for additional servers that they can bring into the LLM. This enables more of an agentic loop since the client doesn't just get to decide which tools are available—the model can search for more things on demand.

**Long-running tasks** will make it easy to do extended operations with MCP, perfect for the agent-powered future we're heading toward.

**Elicitation** will allow servers to go back and ask users for more information when needed, creating a more interactive and intelligent workflow.

The community has grown to over 10,000 MCP server builders, and we're at an interesting inflection point. Initially focused on developers with local experiences, we're now seeing servers hosted in the cloud through remote MCP. This could be a pivotal moment where MCP becomes a true standard for the web for how LLMs interact with online services.

## The Adjacent Possible: Unleashing Human Imagination

The people who are the best users of AI are not coders. They're coaches. They aren't developers or software engineers. They're teachers and mentors and people who have learned to get exceptional output out of other intelligences.

And so where could AI go? Well, it's really a function of who can get unleashed. Right now, the primary limitation is the limits of human imagination. And as we unleash and ignite and spark more humans imaginations, the kinds of applications that are possible or they're unthinkable, not because they're technologically impossible, but because they never occur to us personally.

One of my favorite quotes is a Nobel Prize-winning economist named Thomas Shelling. He said "no matter how heroic a man's imagination he could never think of that which would not occur to him."

If you take as a premise that the imagination space as a function of what would occur to various individuals then as we equip different individuals what we can imagine collectively expands.

In innovation studies has been called the adjacent possible for a long time. What is possible is just adjacent to what is. And as we increase adoption and increase fluency and competency and increasingly mastery of AI collaboration, then we're increasing the adjacent possible.

And it's really important that you exercise through implementing some of the things you hear. And perhaps the most important thing you could do with this video is actually hit stop and do something that's already blown your mind.

## Getting Started: Your Next Steps

If you're new to MCP and want to get involved, start by looking at an existing server that's online. Play around with it. See how it works with Claude AI or Claude Desktop if you want to experiment with local MCPs. Get a feel for that interaction pattern first, and it'll make it much easier to build your own.

Start with the classic hello world approach. Create one tool that just responds with "hello world." Do the same thing for prompts and resources. Try the very basic thing for each before going into anything more complex. Once you get a feel for it, you'll realize how easy it is.

Within ten minutes, you can have something working. Just start local, use Claude Code, and build an MCP server from there. Look at existing servers, see what they do, and make modifications from there. You can even paste the MCP documentation into Claude and ask it to make you a server—it'll grab the docs, bring them in, and create an easy example to get you started.

The future of AI isn't about the technology getting smarter—it's about us getting better at being coaches, teachers, and collaborators with this new form of intelligence. When you understand that AI is good people but bad software, everything changes. You stop expecting it to read your mind and start treating it like the enthusiastic, capable intern it truly is.

But remember to manage those context windows wisely. When you change topics or find the conversation getting unwieldy, start fresh. Your AI will thank you with better performance, and you'll get the sharp, focused responses you're looking for.

Remember: the crazy thing that I've learned is AI demonstrates 100% of the predominant human biases. The good news there is if you have learned how to work with this weird intelligence called humanity, you have everything you need to know to work with this weird intelligence called artificial intelligence.

---

## Article Metadata

**Topic:** context engineering

**Generated:** 2025-10-20 09:22:20

**Sources:**

1. [Stanford's Practical Guide to 10x Your AI Productivity | Jeremy Utley](https://www.youtube.com/watch?v=yMOmmnjy3sE)
   - Channel: EO
   - Views: 400,988
   - Comments: 427

2. [Why LLMs get dumb (Context Windows Explained)](https://www.youtube.com/watch?v=TeQDr4DkLYo)
   - Channel: NetworkChuck
   - Views: 152,251
   - Comments: 318

3. [The Model Context Protocol (MCP)](https://www.youtube.com/watch?v=CQywdSdi5iA)
   - Channel: Anthropic
   - Views: 208,643
   - Comments: 240

**Cost Summary:**

- Total Input Tokens: 25,151
- Total Output Tokens: 14,451
- Total Tokens: 39,602
- **Total Cost: $0.2922**
- Model: Claude Sonnet 4

