# Why MCP Really Is a Big Deal: The Professional's Guide to Agentic AI

Model. Context. Protocol. It really is a big deal, but I think most people are missing the point here. Everybody's talking about enhancing desktop applications with agentic functionality. But if you want to write agentic AI applications at work like a professional, you're going to need a broader vision.

In order for me to give you that vision, I'm going to need to explain to you how it works. And here's a hint: comparing it to the USB-C of AI applications is probably not going to be helpful. Didn't help me, I don't think it's going to help you.

## Understanding the Fundamental Problem

Let's start by remembering how an LLM basically works from an outside perspective. You have a prompt and you send that into an LLM. Out of that LLM, you get a response. 

Now, there are two problems here. That response is just words. And if words are what you want, you're doing fine. But what if you want to do something? That's what agentic AI is all about. You want to cause effects out in the world. The AI needs to be able to take those actions or invoke what we call tools.

It also needs more up-to-date information or maybe just broader information than what's available in that core foundation model. And that's great. This guy is here as an API out on the internet. You might have wrapped that with the so-called Retrieval Augmented Generation pattern. Some people say RAG is old and busted and yesterday's news. In fact, in enterprise context, you may well be using this pattern and there's not a thing in the world wrong with that to bring the data of the enterprise into the context that the LLM can work with.

Whether RAG is there or not doesn't really matter. The fact is there are going to be other resources in our world that we're going to need to get into the prompt, into the scope of what the model can deal with. And these can be anything:

- Files
- Binaries 
- Databases
- Things happening in a Kafka topic (that's even a pretty likely source of resources)

There's just this data out in the world that the agent needs to be aware of. These are two things that are just not going to be present in the base foundation model.

## The Memory Challenge: Why Context Windows Matter

But before we dive into MCP's architecture, there's a crucial limitation you need to understand about how LLMs work. Sometimes when you're talking to an LLM like ChatGPT, it gets kind of dumb, right? You'll be deep into a conversation that you can't even scroll to the top of because it's so long and it starts to say weird things. It hallucinates. It forgets what you're talking about. It makes stuff up and it's stinking slow. Why is this happening? Context windows.

LLMs like ChatGPT, Gemini, Claude, even local models like Llama or DeepSeek, they're kind of like us, you and me, in that they have memories. Short-term memory, which means they can remember things. That's awesome. But also, sometimes they can forget stuff.

Let's say you and me, we're having some coffee and we're talking for about 15 minutes. In that short amount of time, we remember pretty much everything. I remember that story you told. You remember that dumb joke I said. But you're pretty fun to talk to. So, we end up talking for an hour, 2 hours, 3 hours, and at that point, it's kind of hard to keep track of stuff. I forget that amazing point you made. And sometimes we forget the entire point of the conversation.

ChatGPT does the same thing. It's like you and your wife fighting for so long that you forget what you're fighting about to begin with. The longer that conversation goes on, the more things you say, the more things it says back to you, it has to store all of that in its short-term memory. And that short-term memory has a limit. That limit is its context window.

### How Context Windows Actually Work

Context windows are measured in tokens - that's how an AI counts the words you say to it. A sentence might be 133 characters or 26 words, but an LLM just cares about tokens. That same sentence might be 38 tokens. Notice it might do an entire word as a token. It might do a space and a word or just one comma as a token.

A lot of things can fill up the context window. The obvious things are things we say and the things it says back. But there also might be system prompts, which are instructions for our LLMs. These you might explicitly give to it or it's included by default. You never see it. You also might give it documents. You might paste a PDF or an Excel spreadsheet. That'll take up some more tokens. And when you're doing some live coding, the code is taking up tokens filling up that context window.

### The Attention Problem

What's fascinating is how LLMs pay attention. When you say something to an LLM like, "Hey, I want coffee, but caffeine makes me jittery. What should I get?" It will do something eerily similar to how we process and think. It will use some fancy semantic math to decide which of these words is important, which is relevant both to the context of your entire conversation and to how the words relate to each other.

They essentially assign attention scores saying, "Hey, in this conversation, coffee is high, caffeine is high, jittery." But words like "I" or "me" kind of low relevance to the context. And we kind of do the same thing. We only remember the things that are relevant.

But here's the kicker: this process is pretty complex. All this math to assign attention scores. And it does this every time you send something to the LLM, every time you add to the conversation. Those larger contexts not only have insane memory requirements, they also have some pretty healthy computational requirements. Every time you add to that conversation, that math problem that has to run to figure out what's important gets bigger and it requires more processing power.

There was a paper released called "Lost in the Middle" and it showed us how LLMs are kind of like us with paying attention. Just like when someone watches a long movie, they'll watch the first part then fall asleep and then wake up at the end. In the same way, conversations with LLMs with large context, the models were more accurate with info at the beginning and even with info at the end, but in the middle, huge drop off. LLMs are falling asleep during a conversation. Kind of.

This is why when you change an idea, when it's a significant shift from what you're currently talking about, you should start a new chat. The performance will be so much better.

## The MCP Architecture

Now, let's talk about a little bit of architecture. What we're doing is building an agent. You could think of it as a microservice. There's nothing particularly exotic about this. But in MCP terms, this is called the **host application**. And the host application uses the MCP client library to create an instance of a client in there.

Out here, we're going to create an **MCP server**. This may be a server that already exists that somebody else has built that we want to take advantage of to bring agentic functionality into our service, or this could be a server that we ourselves are creating.

Inside the server, what do we have? Well, we've got access to tools, resources, prompts, capabilities that the server makes available and even describes to the outside world. So this is a server process. There's a URL, port, etc, and a variety of well-known RESTful endpoints described by the MCP specification that are implemented by this server, including this capabilities list that tells the world, tells the host application, tells the client, whether there are tools present, what sort of resources might be available, what prompts it has, etc, etc.

### Connection Options

The connection between these two things, between client and server, can be two things:

1. **Standard IO**: If this is a process running locally on my laptop and I've got some LLM host application, like say, Claude Desktop or something, that's something that shows up in a lot of the examples, they can just communicate via pipes and standard IO. We don't want that. That's not kind of what we're interested in in the model I'm trying to give you here.

2. **HTTP and Server Sent Events**: We also have this as an option, and the messages being exchanged here are going to be in JSON RPC. Now, I will not apologize for those technology choices because I didn't make them. Yes, they have raised the occasional eyebrow, but this is what we've got.

There's a little bit of sort of protocol for a client announcing itself to the server and then establishing communications. There are ways for servers to send asynchronous notifications back to the client. So, a relatively rich setup here for client and server to talk.

## A Real-World Example: Building an Appointment Service

But what does it do? Let's walk through an example. I think that would be helpful.

Let's say we're building a service for making appointments. Sort of generalized meet with somebody, some group of people at some place, and not necessarily a conference room in the office, but maybe we're getting coffee. Maybe we're getting breakfast. Maybe it's a romantic dinner with your spouse.

I've just described a number of tools and resources that are necessary to make that happen. Let's think about that:

### Required Tools and Resources

**Tools I need:**
- Create a calendar invite
- Calendar API integration
- Make a reservation at a restaurant

**Resources I need:**
- See when my calendar is free
- Maybe access to the counterparty's calendar (depending on permissions)
- Places I might meet
- What restaurants, coffee shops, breakfast joints are in the area

These are resources that I wanna make available to my agentic application. I could just do all that stuff, do the calendar integration, go talk to Yelp or whatever APIs I wanna do and bake that into my agent, but then it's locked there and nobody else can get at that unless they've got that code. So the whole idea of MCP is I'm putting those things in here.

### The Workflow in Action

Let's go through a workflow of how this might work. A prompt comes in, and that prompt from the user is something like, "I wanna have coffee with Peter next week."

Okay, well, you just ask the LLM, it's like, "Who's Peter? Where's coffee? I can't help you with this." But here we can start to do better.

**Step 1: Capability Discovery**
This application, the host, the client, whatever you wanna call it, can say, "What capabilities do you have?" It knows the URL of this agent. You've had to tell it and maybe very tactically there's a properties file somewhere with a little list of the URLs of servers that are registered with the agent.

**Step 2: Resource Interrogation**
And so it can interrogate the capabilities and see, "Oh, you have resources. Okay. Let me get a list of your resources" which will include text descriptions of each resource. And it's important when writing the server, when building a server to make those good.

**Step 3: AI-Powered Resource Selection**
I can take my prompt. I don't know, I'm just a poor little agentic application. I don't know how to figure out from the input whether I need any of those resources, but I can ask my model. I can say, "You know what, on pass number one, I'll say, here is what my user said. Here is a list of resources: resource one, resource two, resource three. Do I need these?"

We are telling the LLM, "I got this request. I have things like this. Do you think I should go get anything from them?" We submit this as a prompt up to our LLM and it tells us in return, "Yes, you need resource two. That resource two, that list of coffee shops in the area, that looks super interesting. Please give me that."

**Step 4: Resource Retrieval and Integration**
And so now my client says, "Oh, resource two? I know where that is. I'll just go ask my MCP server for the details of resource two." Maybe passing some parameters, maybe not. And then I will get that text back or whatever that data is. I'll get that back and serialize it as text or otherwise attach it to my next prompt.

Where I say, again, "Here is my user prompt. And now here is the resource data." And I provide that data in detail and then ask, "What should I do as a result?" That's how I get the model to help me interpret the resources.

### Tool Invocation Made Simple

How do I interpret the tools? Well, the good news is, so this call is gonna go back to that same LLM and the APIs now for the foundation models, the biggies, I can actually put the description of the tools in the API call. I don't even have to mess with the prompt or anything. It's structured data that goes in there, the name of the tool, the URL, the schema of the parameters, all that.

And in the reply, that tells me if there's a tool I should invoke, it'll say, "Yes, invoke this tool, pass these parameters." I don't have to write any of the code to parse any of the stuff out because I don't know how to do that. That's all very difficult stuff that LLMs are wonderful at. And those APIs will help me with that tool invocation.

They won't call them, okay? ChatGPT, Claude, Gemini, they're not gonna go invoke some URL inside my network and go do something. You know, that's a little bit Skynet-y there, right? But they're gonna tell me, "I recommend you do this." And now my client code gets to make the decision, maybe asking the user first, maybe not, to go call that tool and cause the effect out in the world.

## The Real Power: Composability and Discoverability

So you can kind of see how this works. So instead of just baking all this code in here, we have this that is now pluggable and discoverable. I don't need to know very much about what this tool does. I just plug it in. I just say, "Hey, you have this agent registered with you, go find out about it, go through this process, and you get its functionality."

They're also **composable**. The server itself can be a client. So, let's say I had some data source that I knew was in Kafka out there, and I don't wanna go write a bunch of extra Kafka code to go do that in here. Well, I can just then go use, let's say the Confluent MCP server and connect to that topic or even do actually a bunch more stuff. It's a pretty cool MCP server. If Kafka and Confluent are a part of your life, it's good stuff.

But if I just need to consume from a Kafka topic, this server itself gets to be a client of another server. So I've got:

- **Pluggability**
- **Discoverability** 
- **Composability**

These are huge benefits. These are things that we want in our code.

## Working with AI: From Technology to Teammate

Here's something crucial to understand about working with agentic AI systems: AI is bad software but it's good people. You have to know that at its basic level, AI wants to be helpful. And so it's predisposed to say yes. It's a super eager, super enthusiastic intern who's tireless, who's capable, who will do a bunch of work, but they're not really great at pushing back.

The people who are the best users of AI are not coders, they're coaches. And so, if you aren't careful, AI will gaslight you. AI knows most humans don't want honest feedback. They want to be told they did a good job. So the AI goes, "Great job, buddy." It doesn't mean that you actually did a good job.

When I realize that I'm dealing with a good person but bad software, then it changes how I approach it and I ask for volume and I iterate and I ask it to try again and I ask it to reconsider. This is part of the core actually of the teammate not technology paradigm.

### Context Engineering: Beyond Basic Prompts

Context engineering is just prompt engineering on steroids. It's basically saying, what are all of the things that I need to give to an AI in order for it to perform the task that I'm asking for it?

Here's a simple example: write me a sales email. That's a prompt. ChatGPT will say, absolutely. Here's a compelling email, and they'll write it immediately. Well, what a lot of people do is they say, it sounds like AI. It doesn't really sound like me. And what I often say is, have you told it what you sound like?

Context engineering, one way to think about it is it's telling AI what you sound like. If you say, "Write me a sales email in line with the voice and brand guidelines I've uploaded," it will write a totally different sales email. But that's just one part of the context. You could also upload a transcript from a prospective customer call and say, "Write me a sales email in the tone of voice from our brand voice guideline that references the discussion that I had with this customer" and then add that also references our product specifications which were referenced in the call.

All of the stuff that are implicit, you actually have to make explicit. And the simplest test for context engineering is actually the test of humanity. Write down your prompt and whatever documentation you provide to an AI and then walk down the hall and give it to a human colleague. If they cannot do the thing you're asking for, you shouldn't be surprised that AI can't do it.

### Essential Techniques for Professional AI Collaboration

**Chain of Thought Reasoning**

When you get an AI to think out loud, so to speak, it meaningfully improves the outputs of the model. It doesn't require some technical wizardry. It requires one additional sentence to whatever prompt you've given it. Give the prompt and then say the following: "Before you respond to my query, please walk me through your thought process step by step."

Why does that work? It comes back to the fundamental architecture of large language models. What's happening when a language model is generating a response is it's predicting its next word. A language model does not premeditate a response to you. When you ask a model to think out loud or use chain of thought reasoning, it gives the model the opportunity to bake all of its thought process about the task into its own answer.

**Few Shot Prompting**

The idea with few shot prompting is an AI is an exceptional imitation engine. If you don't give an example, it imitates the internet, but it doesn't do much more than that. The notion of few shot prompting is effectively saying here's what a good output looks like to me.

For example, what are my five greatest hits of emails that I'm really proud of that I think do a good job of conveying my intent or tone or personality? Why not include those emails in my prompt for an email? If you don't give any guidance, it's going to sound like whatever it thinks the average kind of response should sound like and most of the time its intuition is wrong.

**Reverse Prompting**

This is basically asking the model to ask you for the information it needs. If you ask a model to write a sales email, it's going to make numbers up. But if you reverse prompt the model and say at the end of your prompt: "Before you get started, ask me for any information you need to do a good job."

The model will first walk you through its thought process and then instead of writing the email, it'll say, "I'm going to need the most recent sales figures to be able to write this email. Can you tell me how much you sold of this SKU in Q2 last year?" You basically give the model permission to ask you questions.

**Role Assignment**

Assigning a role is one of the most foundational techniques that you can leverage because it's effectively telling the AI where in its knowledge it should focus. If you say you're a teacher, you're a philosopher, you're a reporter, you're a theatrical performer, molecular biologist, each of those titles triggers all sorts of deep associations with knowledge on the internet.

Better than just a generic prompt is saying "I'd like you to be a professional communications expert." And if you have a favorite professional communications expert, use them. "I'd like you to take on the mindset of Dale Carnegie, the author of How to Win Friends and Influence Others. How would Dale Carnegie think about this?"

## Managing Context Windows in MCP Applications

Understanding context windows becomes crucial when building professional MCP applications. Remember, every resource you pull from an MCP server, every tool description, every piece of contextual information you provide - it all consumes tokens in your context window.

This is where the composability of MCP really shines. Instead of cramming everything into one massive conversation, you can design your MCP servers to provide focused, relevant information. When your appointment booking agent needs restaurant information, it doesn't need to load your entire calendar history. It just needs what's relevant for that specific request.

The key is designing your MCP resources with context efficiency in mind. Make your resource descriptions clear and concise. Structure your data so that the AI can quickly identify what's relevant. And remember that rule about starting new conversations when you shift topics? The same principle applies to MCP workflows - different types of requests might benefit from fresh context.

## MCP in Practice: The Professional Advantage

When you understand both MCP's technical architecture and these AI collaboration principles, you start to see the real power. MCP isn't just about connecting tools and resources—it's about creating a professional-grade foundation for building AI systems that can actually work alongside humans effectively.

The composability that MCP provides means you can build sophisticated agentic applications that leverage the best practices of AI collaboration. Your MCP servers can implement context engineering principles, use chain of thought reasoning in their tool descriptions, and provide the kind of structured, discoverable interfaces that make AI systems truly professional.

Think about our appointment booking example again. With proper context engineering, your MCP server could provide not just calendar data, but contextual information about meeting preferences, past successful bookings, and even personality profiles of meeting participants. The AI agent can then use chain of thought reasoning to walk through the decision-making process of selecting the best meeting time and venue.

But remember the attention problem. If you're building an MCP server that returns massive amounts of data, you're potentially creating a situation where the AI will "fall asleep in the middle" of processing that information. Design your resources to be focused and relevant. If you need to provide extensive information, consider breaking it into multiple, smaller resources that can be accessed as needed.

## The Bigger Picture

So, I hope you can see now how this really is a big deal. There's a broader vision here than just enhancing a desktop application with some way to help me write code locally. This is really a gateway to building true agentic AI in the enterprise, in a professional setting.

Right now, the primary limitation is the limits of human imagination. And as we unleash and ignite and spark more humans' imaginations, the kinds of applications that are possible—they're unthinkable, not because they're technologically impossible, but because they never occur to us personally.

As a Nobel Prize-winning economist named Thomas Schelling said, "No matter how heroic a man's imagination, he could never think of that which would not occur to him." If you take as a premise that the imagination space is a function of what would occur to various individuals, then as we equip different individuals, what we can imagine collectively expands.

MCP provides the technical foundation, but the real breakthrough comes when you combine it with professional AI collaboration techniques and a deep understanding of how AI systems actually process and remember information. You're not just building tools—you're building intelligent teammates that can discover, compose, and collaborate in ways we're only beginning to imagine.

The context window limitations we discussed aren't just technical constraints—they're design opportunities. They force us to think more carefully about what information is truly relevant, how to structure our interactions for maximum effectiveness, and when to start fresh conversations for optimal performance.

So check it out, get started, and as always, let me know in the comments what you build. That is really cool stuff.

---

## Article Metadata

**Topic:** context engineering

**Generated:** 2025-10-17 09:18:59

**Sources:**

1. [Why MCP really is a big deal | Model Context Protocol with Tim Berglund](https://www.youtube.com/watch?v=FLpS7OfD5-s)
   - Channel: Confluent Developer
   - Views: 572,323
   - Comments: 738

2. [Stanford's Practical Guide to 10x Your AI Productivity | Jeremy Utley](https://www.youtube.com/watch?v=yMOmmnjy3sE)
   - Channel: EO
   - Views: 396,738
   - Comments: 423

3. [Why LLMs get dumb (Context Windows Explained)](https://www.youtube.com/watch?v=TeQDr4DkLYo)
   - Channel: NetworkChuck
   - Views: 151,542
   - Comments: 319

**Cost Summary:**

- Total Input Tokens: 21,200
- Total Output Tokens: 12,269
- Total Tokens: 33,469
- **Total Cost: $0.2476**
- Model: Claude Sonnet 4

