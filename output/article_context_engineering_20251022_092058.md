# Why MCP Really Is a Big Deal: A Professional's Guide to Model Context Protocol

Model. Context. Protocol. It really is a big deal, but I think most people are missing the point here. Everybody's talking about enhancing desktop applications with agentic functionality. But if you want to write agentic AI applications at work like a professional, you're going to need a broader vision.

In order for me to give you that vision, I'm going to need to explain to you how it works. And here's a hint: comparing it to the USB-C of AI applications is probably not going to be helpful. Didn't help me, I don't think it's going to help you.

But before we dive into MCP, we need to understand something fundamental about working with AI effectively. As I've learned from working with these systems professionally, AI is bad software but it's good people. The people who are the best users of AI are not coders, they're coaches. They aren't developers or software engineers. They're teachers and mentors and people who have learned to get exceptional output out of other intelligences.

## The Fundamental Problem with LLMs

Now, let's start by remembering how an LLM basically works from an outside perspective, right? You have a prompt and you send that into an LLM. Out of that LLM, you get a response. 

There are two problems here:

**First, that response is just words.** And if words are what you want, you're doing fine. But what if you want to do something? That's what agentic AI is all about. You want to cause effects out in the world. The AI needs to be able to take those actions or invoke what we call tools.

**Second, it needs more up-to-date information** or maybe just broader information than what's available in that core foundation model. And that's great. This guy is here as an API out on the internet. You might have wrapped that with the so-called Retrieval Augmented Generation pattern. Some people say RAG is old and busted and yesterday's news. In fact, in enterprise context, you may well be using this pattern and there's not a thing in the world wrong with that to bring the data of the enterprise into the context that the LLM can work with.

Whether RAG is there or not doesn't really matter. The fact is there are going to be other resources in our world that we're going to need to get into the prompt, into the scope of what the model can deal with. And these can be anything:

- Files
- Binaries  
- Databases
- Things happening in a Kafka topic (that's even a pretty likely source of resources)

There's just this data out in the world that the agent needs to be aware of. These are two things that are just not going to be present in the base foundation model.

## Understanding AI as Your Enthusiastic Intern

Here's something crucial to understand about working with AI systems: you have to know that at its basic level, AI wants to be helpful. And so it's predisposed to say yes. It's a super eager, super enthusiastic intern who's tireless, who's capable, who will do a bunch of work, but they're not really great at pushing back. They're not really great at setting boundaries.

A good friend of mine was trying to build a tool that would help him with his construction business. He asked ChatGPT if ChatGPT could help. And of course it said absolutely let's work on this together and starts creating a plan. And then it got to the point that ChatGPT said check back in a couple of days and I'll have it together. And my friend said, "Is it normal for ChatGPT to ask me to check back in a couple days?" And I just started laughing because I hear this all the time from people.

If AI tells you that, it means it doesn't want to say, "I can't do it." So if you aren't careful, AI will gaslight you. AI knows most humans don't want honest feedback. They want to be told they did a good job. So the AI goes, "Great job, buddy." It doesn't mean that you actually did a good job.

This understanding is crucial when we think about MCP, because the protocol isn't just about technical integration—it's about creating a framework where AI can access the right context and tools to actually be helpful, rather than just appearing helpful.

## The Context Window Problem: Why AI Gets Dumb

Before we dive deeper into MCP's architecture, we need to understand a fundamental limitation that affects all AI systems: context windows. Sometimes when you're talking to an LLM like ChatGPT, it gets kind of dumb, right? You'll be deep into a conversation that you can't even scroll to the top of because it's so long and it starts to say weird things. It hallucinates. It forgets what you're talking about. It makes stuff up and it's stinking slow. Why is this happening? Context windows.

LLMs like ChatGPT, Gemini, Claude, even local models like Llama or DeepSeek, they're kind of like us, you and me, in that they have memories. Short-term memory, which means they can remember things. That's awesome. But also, sometimes they can forget stuff. And it happens like this: Let's say you and me, we're having some coffee and we're talking for about 15 minutes. In that short amount of time, we remember pretty much everything. I remember that story you told. You remember that dumb joke I said. But you're pretty fun to talk to. So, we end up talking for an hour, 2 hours, 3 hours, and at that point, it's kind of hard to keep track of stuff. I forget that amazing point you made.

ChatGPT does the same thing. The longer that conversation goes on, the more things you say, the more things it says back to you. It has to store all of that in its short-term memory. And that short-term memory has a limit. That limit is its context window.

### How Context Windows Work

Context windows are measured in tokens. Tokens are how an AI counts the words you say to it. A sentence might be 133 characters or 26 words, but an LLM just cares about tokens. That same sentence would actually be around 34-38 tokens. Notice it might do an entire word as a token. It might do a space and a word or just one comma as a token.

Different models have different context window sizes:
- GPT-4 is rocking 128,000 tokens
- Claude 3.5 Sonnet has 200,000 tokens  
- Gemini 2.5 from Google has 1 million tokens
- Some newer models are pushing toward 2 million tokens

### The Lost in the Middle Problem

There was a paper released called "Lost in the Middle" and it showed us how LLMs are kind of like us with paying attention. And just like when you watch a long movie, you'll watch the first part then fall asleep and then wake up at the end—that's the context you have. In the same way, conversations with LLMs with large context showed that the models were more accurate with info at the beginning and even with info at the end, but in the middle, huge drop off. And across the board, we saw this U shape.

So, what does that tell us? LLMs are falling asleep during a conversation. Kind of. I'm telling you, LLMs have problems paying attention just like us.

### A Quick Solution

Here's a rule I try to go by when I'm talking with LLMs: when you change an idea, when it's a significant shift from what you're currently talking about, start a new chat. The performance will be so much better. In fact, sometimes when you're talking with other LLMs like Claude, it'll even tell you at the bottom, "Hey, you've been talking for a minute, things are going to slow down. Why don't you go and start a new chat so things can be better?"

This context window limitation is exactly why MCP becomes so important—instead of cramming everything into one massive conversation, we can structure our AI interactions through discrete, focused connections to specific resources and tools.

## The MCP Architecture: How It Actually Works

Let's talk about a little bit of architecture. What we're doing is building an agent. You could think of it as a microservice. There's nothing particularly exotic about this. But, in MCP terms, this is called the **host application**. 

The host application uses the MCP client library to create an instance of a client in there. Out here, we're going to create an **MCP server**. This may be a server that already exists that somebody else has built that we want to take advantage of to bring agentic functionality into our service, or this could be a server that we ourselves are creating.

Inside the server, what do we have? Well, we've got access to tools, resources, prompts, capabilities that the server makes available and even describes to the outside world. So, this is a server process. There's a URL, port, etc, and a variety of well-known RESTful endpoints described by the MCP specification that are implemented by this server, including this capabilities list that tells the world, tells the host application, tells the client, whether there are tools present, what sort of resources might be available, what prompts it has, etc.

### Connection Options

The connection between these two things, between client and server, can be two things:

1. **Standard IO** - So if this is a process running locally on my laptop and I've got some LLM host application, like say, Claude Desktop or something, that's something that shows up in a lot of the examples, they can just communicate via pipes and standard IO. We don't want that. That's not kind of what we're interested in in the model I'm trying to give you here.

2. **HTTP and Server Sent Events** - The messages being exchanged here are going to be in JSON RPC. Now, I will not apologize for those technology choices because I didn't make them. Yes, they have raised the occasional eyebrow, but this is what we've got.

There's a little bit of sort of protocol for a client announcing itself to the server and then establishing communications. There are ways for servers to send asynchronous notifications back to the client. So, a relatively rich setup here for client and server to talk.

## Context Engineering: The Foundation of Professional AI

Before we dive into our MCP example, let's talk about something that's absolutely critical for professional AI applications: context engineering. Context engineering is just prompt engineering on steroids. It's basically saying, what are all of the things that I need to give to an AI in order for it to perform the task that I'm asking for it?

Here's a simple example. "Write me a sales email." That's a prompt. ChatGPT will say, absolutely. Here's a compelling email, you know, and they'll write it immediately. Well, what a lot of people do is they say, you know, it sounds like AI. It doesn't really sound like me. And what I often say is, have you told it what you sound like? Most people go, oh no, I haven't.

Context engineering, one way to think about it is it's telling AI what you sound like. If you say, "Write me a sales email," it will. If you say, "Write me a sales email," in line with the voice and brand guidelines I've uploaded, it will write a totally different sales email. But that's just one part of the context, right? You could also upload a transcript from a prospective customer call and say, "Write me a sales email in the tone of voice from our brand voice guideline that references the discussion that I had with this customer." And then you could add that also references our product specifications whichever were referenced in the call.

Your goal is to have an output is as reliable per your specification as possible. But AI can't read your mind. And for most people when we start working together, what they realize as we start thinking about context engineering is they say, "Oh, I was kind of expecting AI to read my mind." All of the stuff that that are implicit, you actually have to make explicit.

The simplest test for context engineering is actually the test of humanity. Write down your prompt and whatever documentation you provide to an AI and then walk down the hall and give it to a human colleague. If they cannot do the thing you're asking for, you shouldn't be surprised that AI can't do it.

This is where MCP becomes powerful—it provides a standardized way to give AI systems the context they need through discoverable resources and tools, without overwhelming the context window with massive amounts of information all at once.

## A Real-World Example: Building an Appointment Service

Let's walk through an example. I think that would be helpful. Let's say we're building a service for making appointments. Sort of generalized meet with somebody, some group of people at some place, and not necessarily a conference room in the office, but maybe we're getting coffee. Maybe we're getting breakfast. Maybe it's a romantic dinner with your spouse.

I've just described a number of tools and resources that are necessary to make that happen. Let's think about that:

**Tools I need:**
- Create a calendar invite
- Calendar API integration  
- Make a reservation at a restaurant

**Resources I need:**
- See when my calendar is free
- Access to counterparty calendars (depending on permissions)
- Places I might meet - restaurants, coffee shops, breakfast joints in the area

I could just do all that stuff, do the calendar integration, go talk to Yelp or whatever APIs I wanna do and bake that into my agent, but then it's locked there and nobody else can get at that unless they've got that code. So the whole idea of MCP is I'm putting those things in here.

### The Workflow in Action: Advanced Prompting Techniques

Let's go through a workflow of how this might work. A prompt comes in, and that prompt from the user is something like, **"I wanna have coffee with Peter next week."**

Okay, well, you just ask the LLM, it's like, "Who's Peter? Where's coffee? I can't help you with this." But here we can start to do better using several advanced techniques.

**Step 1: Capability Discovery with Chain of Thought Reasoning**

This application, the host, the client, whatever you wanna call it, can say, "What capabilities do you have?" It knows the URL of this agent. You've had to tell it and maybe very tactically there's a properties file somewhere with a little list of the URLs of servers that are registered with the agent.

But here's where we can get smarter. One of the things that cognitive scientists have known for a long time is that human problem solving and decision-making is improved by a phenomenon called thinking out loud. If you actually get a human being to think out loud about their problem, their decision-making improves and their problem solving improves. The weird thing about AI is it's true for AI too. This is what's called chain of thought reasoning.

So instead of just asking for capabilities, we can say: "What capabilities do you have? Before you respond to my query, please walk me through your thought process step by step." That's chain of thought reasoning.

Why does that work? It comes back to the fundamental architecture of large language models. What's happening when a language model is generating a response is it's predicting its next word. A language model does not premeditate a response to you. It's thinking one word at a time. But importantly, when it thinks of the next word, it takes your prompt and all of the text that's generated to generate the next word.

**Step 2: Resource Assessment with Reverse Prompting**

It can interrogate the capabilities and see, "Oh, you have resources. Okay. Let me get a list of your resources" which will include text descriptions of each resource. And it's important when writing the server, when building a server to make those good.

But here's where reverse prompting comes in. Instead of just asking the AI to figure out what resources it needs, we can say: "Here is what my user said. Here is a list of resources: resource one, resource two, resource three. Before you decide what resources to use, ask me for any information you need to do a good job."

This is part of the core actually of the teammate not technology paradigm. If you're working with a junior employee and you're sending them off on a task, what's one thing you're definitely going to say? If you have any questions, don't hesitate to ask me. Any good manager would say that. But sadly, AI in its desire to be a helpful assistant doesn't want to trouble us humans with questions unless we give it permission to ask them.

**Step 3: LLM Decision Making with Role Assignment**

We are telling the LLM, "I got this request. I have things like this. Do you think I should go get anything from them?" But we can make this even more effective by assigning a role.

Assigning a role is one of the most foundational techniques that you can leverage because it's effectively telling the AI where in its knowledge it should focus. So very simply, if you say you're a teacher, you're a philosopher, you're a reporter, you're a theatrical performer, molecular biologist, each of those titles triggers all sorts of deep associations with knowledge on the internet.

So instead of just asking generically, we might say: "You are an expert executive assistant who specializes in calendar management and meeting coordination. Given this request and these available resources, walk me through your thought process step by step and tell me what resources you need."

**Step 4: Resource Retrieval with Few-Shot Prompting**

And so now my client says, "Oh, resource two? I know where that is. I'll just go ask my MCP server for the details of resource two." Maybe passing some parameters, maybe not. And then I will get that text back or whatever that data is.

But here's where few-shot prompting becomes crucial. Few-shot prompting is another very important technique. The idea with few-shot prompting is an AI is an exceptional imitation engine. If you don't give an example, it imitates the internet, but it doesn't do much more than that.

So when we get that resource data back, instead of just saying "here's the data," we might include examples of how we want the AI to interpret and use similar data. What are quintessential examples of the kind of output I want to receive? For example, what are my five greatest hits of calendar coordination that I'm really proud of that I think do a good job of conveying my intent or tone or personality?

**Step 5: Tool Invocation with Advanced Context**

Where I say, again, "Here is my user prompt. And now here is the resource data." And I provide that data in detail and then ask, "What should I do as a result?" That's how I get the model to help me interpret the resources.

The good news is, this call is gonna go back to that same LLM and the APIs now for the foundation models, the biggies, I can actually put the description of the tools in the API call. I don't even have to mess with the prompt or anything. It's structured data that goes in there, the name of the tool, the URL, the schema of the parameters, all that.

And in the reply, that tells me if there's a tool I should invoke, it'll say, "Yes, invoke this tool, pass these parameters." I don't have to write any of the code to parse any of the stuff out because I don't know how to do that. That's all very difficult stuff that LLMs are wonderful at. And those APIs will help me with that tool invocation.

They won't call them, okay? ChatGPT, Claude, Gemini, they're not gonna go invoke some URL inside my network and go do something. You know, that's a little bit Skynet-y there, right? But they're gonna tell me, "I recommend you do this." And now my client code gets to make the decision, maybe asking the user first, maybe not, to go call that tool and cause the effect out in the world.

## The Three Key Benefits: Why This Changes Everything

So you can kind of see how this works. So instead of just baking all this code in here, we have this that is now pluggable and discoverable. I don't need to know very much about what this tool does. I just plug it in. I just say, "Hey, you have this agent registered with you, go find out about it, go through this process, and you get its functionality."

### 1. Pluggability
Instead of hardcoding everything into your agent, you can plug in external servers that provide the functionality you need.

### 2. Discoverability  
Your agent can automatically discover what capabilities are available without you having to know the details upfront.

### 3. Composability
They're also composable. The server itself can be a client. So, let's say I had some data source that I knew was in Kafka out there, and I don't wanna go write a bunch of extra Kafka code to go do that in here. Well, I can just then go use, let's say the Confluent MCP server and connect to that topic or even do actually a bunch more stuff. It's a pretty cool MCP server. If Kafka and Confluent are a part of your life, it's good stuff.

But if I just need to consume from a Kafka topic, this server itself gets to be a client of another server. So I've got pluggability, discoverability, composability, huge benefits. These are things that we want in our code.

## Advanced Techniques for Professional AI Integration

When building professional AI applications with MCP, there are several advanced techniques that can dramatically improve your results:

### Constraint-Based Problem Solving

One of the simplest techniques that we can use is trying on different constraints. One of the best ways you can solve a problem as a human is by forcing yourself to try on a bunch of different constraints. How would Jerry Seinfeld solve this problem? How would your favorite sushi restaurant solve this problem? How would Amazon solve it? How would Elon Musk?

Anytime you make an association, you're colliding different information sources there. The same is true for an AI. An AI is basically making tons of connections through its own neural network. And by giving it a role, you're telling it where do you assume the best source of connection or collision is going to come from?

### Getting Honest Feedback

My kind of hack for getting better feedback from AI is I always instruct the AI: I want you to do your best impression of a cold war era Russian Olympic judge. Be brutal. Be exacting. Deduct points for every minor flinch that you can find. I can handle difficult feedback.

And then it's of course hilarious because it'll say now channeling my inner Bolshoi, you know, it'll say something silly and then it gives me like a 42. That is much better because now I have an insightful critical perspective.

### Preserving Critical Thinking

Some people are concerned about cognitive offloading—this observed phenomenon that humans actually kind of stop thinking or as one researcher put it fall asleep at the wheel and people are concerned right now is AI just making us dumber.

My feeling is AI is a mirror and to people who want to offload work and who want to be lazy it will help you to people who want to be more cognitively sharp and critical thinkers it will help you do that too. And so, for example, if you want to preserve or strengthen your critical thinking, part of your custom instructions should be some version of the following: I'm trying to stay a critical and sharp analytical thinker. Whenever you see opportunities in our conversations, please push my critical thinking ability.

Now, AI will do it.

## Managing Context Windows in Professional Applications

When working with MCP in production environments, understanding how to manage context windows becomes crucial. A few things can fill up the context window beyond just conversation:

- **System prompts** - Instructions for our LLMs that you might explicitly give to it or are included by default
- **Documents** - When you paste a PDF or an Excel spreadsheet, that takes up tokens
- **Code** - When you're doing some vibe coding, the code is taking up tokens filling up that context window

The longer a conversation gets, the more computational requirements it has. Every time you add to that conversation, the math problem that has to run to figure out what's important gets bigger and it requires more GPU power. And that is why in those larger conversations, the LLM starts to hallucinate and it seems just a bit more slow.

This is where MCP's architecture really shines. Instead of dumping everything into one massive context window, you're making targeted calls to specific resources and tools only when needed. This keeps your context focused and your AI performant.

## The Bigger Picture: Professional Agentic AI

So, I hope you can see now how this really is a big deal. There's a broader vision here than just enhancing a desktop application with some way to help me write code locally. This is really a gateway to building true agentic AI in the enterprise, in a professional setting. That is really cool stuff.

Right now, the primary limitation is the limits of human imagination. And as we unleash and ignite and spark more humans imaginations, the kinds of applications that are possible or they're unthinkable, not because they're technologically impossible, but because they never occur to us personally.

One of my favorite quotes is a Nobel Prize-winning economist named Thomas Shelling. He said no matter how heroic a man's imagination he could never think of that which would not occur to him. If you take as a premise that the imagination space as a function of what would occur to various individuals then as we equip different individuals what we can imagine collectively expands.

In innovation studies has been called the adjacent possible for a long time. What is possible is just adjacent to what is. And as we increase adoption and increase fluency and competency and increasingly mastery of AI collaboration, then we're increasing the adjacent possible.

Model Context Protocol isn't just about making your desktop apps a little smarter. It's about creating a foundation for professional-grade agentic AI systems that can integrate with your existing infrastructure, discover capabilities dynamically, and compose complex workflows from simple, reusable components. When combined with advanced prompting techniques like chain of thought reasoning, reverse prompting, few-shot prompting, and proper context engineering—all while managing context windows effectively—MCP becomes the backbone of truly intelligent, context-aware AI applications.

So check it out, get started, links below with great help. And as always, let me know in the comments what you build. And perhaps the most important thing you could do with this article is actually stop reading and do something that's already blown your mind.

---

## Article Metadata

**Topic:** context engineering

**Generated:** 2025-10-22 09:20:58

**Sources:**

1. [Why MCP really is a big deal | Model Context Protocol with Tim Berglund](https://www.youtube.com/watch?v=FLpS7OfD5-s)
   - Channel: Confluent Developer
   - Views: 579,714
   - Comments: 743

2. [Stanford's Practical Guide to 10x Your AI Productivity | Jeremy Utley](https://www.youtube.com/watch?v=yMOmmnjy3sE)
   - Channel: EO
   - Views: 404,688
   - Comments: 428

3. [Why LLMs get dumb (Context Windows Explained)](https://www.youtube.com/watch?v=TeQDr4DkLYo)
   - Channel: NetworkChuck
   - Views: 152,768
   - Comments: 318

**Cost Summary:**

- Total Input Tokens: 22,013
- Total Output Tokens: 13,577
- Total Tokens: 35,590
- **Total Cost: $0.2697**
- Model: Claude Sonnet 4

