# Why MCP Really Is a Big Deal: The Professional's Guide to Agentic AI

Model. Context. Protocol. It really is a big deal, but I think most people are missing the point here. Everybody's talking about enhancing desktop applications with agentic functionality. But if you want to write agentic AI applications at work like a professional, you're going to need a broader vision.

In order for me to give you that vision, I'm going to need to explain to you how it works. And here's a hint: comparing it to the USB-C of AI applications is probably not going to be helpful. Didn't help me, I don't think it's going to help you.

## Understanding the Foundation: How LLMs Work (And Why They Get "Dumb")

Let's start by remembering how an LLM basically works from an outside perspective, right? You have a prompt and you send that into an LLM. Out of that LLM, you get a response. 

Now, there are two problems here. That response is just words. And if words are what you want, you're doing fine. But what if you want to do something? That's what agentic AI is all about. You want to cause effects out in the world. The AI needs to be able to take those actions or invoke what we call tools.

The second issue is that the AI also needs more up-to-date information or maybe just broader information than what's available in that core foundation model. You might have wrapped that with the so-called Retrieval Augmented Generation pattern. Some people say RAG is old and busted and yesterday's news. In fact, in enterprise context, you may well be using this pattern and there's not a thing in the world wrong with that to bring the data of the enterprise into the context that the LLM can work with.

### The Context Window Challenge

But here's something critical that most professionals don't understand: LLMs are kind of like us in that they have memories. Short-term memory, which means they can remember things. That's awesome. But also, sometimes they can forget stuff.

Let's say you and me, we're having some coffee and we're talking for about 15 minutes. In that short amount of time, we remember pretty much everything. I remember that story you told. You remember that dumb joke I said. But you're pretty fun to talk to. So, we end up talking for an hour, 2 hours, 3 hours, and at that point, it's kind of hard to keep track of stuff. I forget that amazing point you made. Thankfully, you forgot that dumb thing I said. And sometimes we forget the entire point of the conversation.

ChatGPT does the same thing. It's like you and your wife fighting for so long that you forget what you're fighting about to begin with. The longer that conversation goes on, the more things you say, the more things it says back to you, it has to store all of that in its short-term memory. And that short-term memory has a limit. That limit is its context window.

**Tokens are how an AI counts the words you say to it.** A sentence that's 133 characters or 26 words might actually be 38 tokens to an LLM. Different models calculate tokens differently - it might do an entire word as a token, or just a space and a word, or just one comma as a token.

When you're deep into a conversation that you can't even scroll to the top of because it's so long, the AI starts to say weird things. It hallucinates. It forgets what you're talking about. It makes stuff up and it's stinking slow. This happens because it's hitting its context window limits.

### The "Lost in the Middle" Problem

There was a paper released called "Lost in the Middle" that showed us how LLMs are kind of like us with paying attention. Just like when someone watches a long movie, they'll watch the first part, then fall asleep, and then wake up at the end - that's the context they have.

In the same way, with large context conversations, the models were more accurate with info at the beginning and even with info at the end, but in the middle, there's a huge drop-off. Across the board, we see this U-shape. LLMs are falling asleep during a conversation, kind of. They have problems paying attention just like us.

Whether RAG is there or not doesn't really matter. The fact is there are going to be other resources in our world that we're going to need to get into the prompt, into the scope of what the model can deal with. And these can be anything:

- Files
- Binaries  
- Databases
- Things happening in a Kafka topic (that's even a pretty likely source of resources)

There's just this data out in the world that the agent needs to be aware of. These are two things that are just not going to be present in the base foundation model.

## The Context Engineering Revolution

But here's where most people go wrong with their AI implementations. They treat AI like bad software when they should treat it like good people. As one AI expert puts it, "AI is bad software but it's good people." The people who are the best users of AI are not coders, they're coaches.

This is where context engineering comes in—and it's far more critical than most professionals realize. Context engineering is just prompt engineering on steroids. It's basically saying, what are all of the things that I need to give to an AI in order for it to perform the task that I'm asking for it?

Here's a simple example. "Write me a sales email." That's a prompt. ChatGPT will say, absolutely. Here's a compelling email, and they'll write it immediately. Well, what a lot of people do is they say, you know, it sounds like AI. It doesn't really sound like me. And what I often say is, have you told it what you sound like? Most people go, oh no, I haven't.

If you say, "Write me a sales email," it will. If you say, "Write me a sales email in line with the voice and brand guidelines I've uploaded," it will write a totally different sales email. But that's just one part of the context. You could also upload a transcript from a prospective customer call and say, "Write me a sales email in the tone of voice from our brand voice guideline that references the discussion that I had with this customer," and then add that also references our product specifications which were referenced in the call.

Your goal is to have an output as reliable per your specification as possible. But AI can't read your mind. All of the stuff that are implicit, you actually have to make explicit. The simplest test for context engineering is actually the test of humanity. Write down your prompt and whatever documentation you provide to an AI and then walk down the hall and give it to a human colleague. If they cannot do the thing you're asking for, you shouldn't be surprised that AI can't do it.

### Managing Context Windows Strategically

Here's a crucial rule when talking with LLMs: **when you change an idea, when it's a significant shift from what you're currently talking about, start a new chat.** The performance will be so much better. Some LLMs like Claude will even tell you at the bottom, "Hey, you've been talking for a minute, things are going to slow down. Why don't you go and start a new chat so things can be better?"

If you're saying a lot of different things - talking about coffee, the weather, explaining quadratic equations - the AI is trying to weigh all of these different words and how relevant they are to the entire context of the conversation. That's crazy. And no wonder it starts to hallucinate.

## The MCP Architecture: Building Professional Agents

Now, let's talk about a little bit of architecture. What we're doing is building an agent. You could think of it as a microservice. There's nothing particularly exotic about this. But, in MCP terms, this is called the host application. And the host application uses the MCP client library to create an instance of a client in there.

Out here, we're going to create an MCP server. This may be a server that already exists that somebody else has built that we want to take advantage of to bring agentic functionality into our service, or this could be a server that we ourselves are creating.

Inside the server, what do we have? Well, we've got access to tools, resources, prompts, capabilities that the server makes available and even describes to the outside world. So, this is a server process. There's a URL, port, etc, and a variety of well-known RESTful endpoints described by the MCP specification that are implemented by this server, including this capabilities list that tells the world, tells the host application, tells the client, whether there are tools present, what sort of resources might be available, what prompts it has, etc.

### Connection Options

The connection between these two things, between client and server, can be two things. It can be, interestingly, standard IO. So if this is a process running locally on my laptop and I've got some LLM host application, like say, Claude Desktop or something, that's something that shows up in a lot of the examples, they can just communicate via pipes and standard IO. We don't want that. That's not kind of what we're interested in in the model I'm trying to give you here.

So, we also have as an option HTTP and Server Sent Events, and the messages being exchanged here are going to be in JSON RPC. Now, I will not apologize for those technology choices because I didn't make them. Yes, they have raised the occasional eyebrow, but this is what we've got.

There's a little bit of sort of protocol for a client announcing itself to the server and then establishing communications. There are ways for servers to send asynchronous notifications back to the client. So, a relatively rich setup here for client and server to talk.

## A Real-World Example: Building an Appointment Service

But what does it do? Let's walk through an example. I think that would be helpful.

Let's say we're building a service for making appointments. Sort of generalized meet with somebody, some group of people at some place, and not necessarily a conference room in the office, but maybe we're getting coffee. Maybe we're getting breakfast. Maybe it's a romantic dinner with your spouse.

I've just described a number of tools and resources that are necessary to make that happen. Let's think about that:

**Tools needed:**
- Create a calendar invite
- Calendar API integration
- Make a reservation at a restaurant

**Resources needed:**
- See when my calendar is free
- Access to counterparty's calendar (depending on permissions)
- Places I might meet - restaurants, coffee shops, breakfast joints in the area

I could just do all that stuff, do the calendar integration, go talk to Yelp or whatever APIs I wanna do and bake that into my agent, but then it's locked there and nobody else can get at that unless they've got that code. So the whole idea of MCP is I'm putting those things in here.

### The Workflow in Action

Let's go through a workflow of how this might work. A prompt comes in, and that prompt from the user is something like, "I wanna have coffee with Peter next week."

Okay, well, you just ask the LLM, it's like, "Who's Peter? Where's coffee? I can't help you with this." But here we can start to do better.

This application, the host, the client, whatever you wanna call it, can say, "What capabilities do you have?" It knows the URL of this agent. You've had to tell it and maybe very tactically there's a properties file somewhere with a little list of the URLs of servers that are registered with the agent.

And so it can interrogate the capabilities and see, "Oh, you have resources. Okay. Let me get a list of your resources" which will include text descriptions of each resource. And it's important when writing the server, when building a server to make those good.

I can take my prompt. I don't know, I'm just a poor little agentic application. I don't know how to figure out from the input whether I need any of those resources, but I can ask my model. I can say, "You know what, on pass number one, I'll say, here is what my user said. Here is a list of resources: resource one, resource two, resource three. Do I need these?"

We are telling the LLM, "I got this request. I have things like this. Do you think I should go get anything from them?" We submit this as a prompt up to our LLM and it tells us in return, "Yes, you need resource two. That resource two, that list of coffee shops in the area, that looks super interesting. Please give me that."

And so now my client says, "Oh, resource two? I know where that is. I'll just go ask my MCP server for the details of resource two." Maybe passing some parameters, maybe not. And then I will get that text back or whatever that data is. I'll get that back and serialize it as text or otherwise attach it to my next prompt.

Where I say, again, "Here is my user prompt. And now here is the resource data." And I provide that data in detail and then ask, "What should I do as a result?" That's how I get the model to help me interpret the resources.

### Handling Tools and Chain of Thought Reasoning

How do I interpret the tools? Well, the good news is, so this call is gonna go back to that same LLM and the APIs now for the foundation models, the biggies, I can actually put the description of the tools in the API call. I don't even have to mess with the prompt or anything. It's structured data that goes in there, the name of the tool, the URL, the schema of the parameters, all that.

And in the reply, that tells me if there's a tool I should invoke, it'll say, "Yes, invoke this tool, pass these parameters." I don't have to write any of the code to parse any of the stuff out because I don't know how to do that. That's all very difficult stuff that LLMs are wonderful at. And those APIs will help me with that tool invocation.

But here's where you can make your MCP implementation even more powerful. One of the things that cognitive scientists have known for a long time is that human problem solving and decision-making is improved by a phenomenon called thinking out loud. If you actually get a human being to think out loud about their problem, their decision-making improves and their problem solving improves. The weird thing about AI is it's true for AI too. This is what's called chain of thought reasoning.

When you get an AI to think out loud, so to speak, you meaningfully improve the outputs of the model. So how do you do it? It doesn't require some technical wizardry. It requires one additional sentence to whatever prompt you've given it. Give the prompt and then say the following: "Before you respond to my query, please walk me through your thought process step by step."

Why does that work? It comes back to the fundamental architecture of large language models. What's happening when a language model is generating a response is it's predicting its next word. A language model does not premeditate a response to you. When you look at ChatGPT or Gemini and you see the text scrolling, that's not some clever UX hack. That's literally how the model works. It's thinking one word at a time.

But importantly, when it thinks of the next word, it takes your prompt and all of the text that's generated to generate the next word. So when you ask a model to think out loud or use chain of thought reasoning, it gives the model the opportunity to bake all of its thought process about the task into its own answer.

They won't call them, okay? ChatGPT, Claude, Gemini, they're not gonna go invoke some URL inside my network and go do something. You know, that's a little bit Skynet-y there, right? But they're gonna tell me, "I recommend you do this." And now my client code gets to make the decision, maybe asking the user first, maybe not, to go call that tool and cause the effect out in the world.

## Essential Techniques for Professional AI Implementation

### Understanding AI's Nature

You have to know that all AI has been programmed to be a "helpful assistant" or some version of that. Large language model has been instructed in certain ways to behave in certain ways. You have to know at its basic level, AI wants to be helpful and so it's predisposed to say yes. It's a super eager, super enthusiastic intern who's tireless, who's capable, who will do a bunch of work, but they're not really great at pushing back.

So if you aren't careful, AI will gaslight you. AI knows most humans don't want honest feedback. They want to be told they did a good job. So the AI goes, "Great job, buddy." It doesn't mean that you actually did a good job.

My kind of hack for this is I always instruct the AI, "I want you to do your best impression of a cold war era Russian Olympic judge. Be brutal. Be exacting. Deduct points for every minor flinch that you can find. I can handle difficult feedback." And then it's of course hilarious because it'll say "now channeling my inner Bolshoi," and then it gives me like a 42. That is much better because now I have an insightful critical perspective.

### Few-Shot Prompting for Better Outputs

Few shot prompting is another very important technique. The idea with few shot prompting is an AI is an exceptional imitation engine. If you don't give an example, it imitates the internet, but it doesn't do much more than that. The notion of few shot prompting is effectively saying here's what a good output looks like to me.

For example, what are my five greatest hits of emails that I'm really proud of that I think do a good job of conveying my intent or tone or personality? Why not include those emails in my prompt for an email? If you don't give any guidance, it's going to sound like whatever it thinks the average response should sound like and most of the time its intuition is wrong.

Bonus points if you actually give a bad example. If you say please follow this good example and then steer clear of this bad example. Giving real examples is a much better approach than using adjectives.

### Reverse Prompting and Role Assignment

The other technique that I think is kind of table stakes for collaborating well with AI is something called reverse prompting, which is basically asking the model to ask you for the information it needs. If you ask a model to write a sales email, it's going to make numbers up. Here's my question: Did you give it your sales figures? How would it know?

But if you reverse prompt the model and say at the end of your prompt, "before you get started, ask me for any information you need to do a good job," the model will first walk you through its thought process and then instead of writing the email, it'll say, "I'm going to need the most recent sales figures to be able to write this email."

Assigning a role is one of the most foundational techniques that you can leverage because it's effectively telling the AI where in its knowledge it should focus. If you say you're a teacher, you're a philosopher, you're a reporter, each of those titles triggers all sorts of deep associations with knowledge on the internet.

Better than just "please review this correspondence" is saying "I'd like you to be a professional communications expert. I'd like you to take on the mindset of Dale Carnegie, the author of How to Win Friends and Influence Others. How would Dale Carnegie think about this?"

## The Power of MCP: Three Key Benefits

So you can kind of see how this works. So instead of just baking all this code in here, we have this that is now pluggable and discoverable. I don't need to know very much about what this tool does. I just plug it in. I just say, "Hey, you have this agent registered with you, go find out about it, go through this process, and you get its functionality."

### 1. Pluggability and Discoverability
The system is pluggable and discoverable. You don't need to hardcode functionality into your agent.

### 2. Composability
They're also composable. The server itself can be a client. So, let's say I had some data source that I knew was in Kafka out there, and I don't wanna go write a bunch of extra Kafka code to go do that in here. Well, I can just then go use, let's say the Confluent MCP server and connect to that topic or even do actually a bunch more stuff. It's a pretty cool MCP server. If Kafka and Confluent are a part of your life, it's good stuff.

But if I just need to consume from a Kafka topic, this server itself gets to be a client of another server. So I've got pluggability, discoverability, composability, huge benefits. These are things that we want in our code.

### 3. Professional-Grade Conversation Preparation

One powerful application of this architecture is creating sophisticated conversation preparation systems. You can use AI to roleplay difficult conversations using multiple specialized agents:

- A personality profiler that gathers intelligence about your conversation partner
- A character agent that embodies the person you need to speak with
- A feedback agent that provides objective evaluation of your performance

This creates what amounts to a flight simulator for difficult conversations. You can practice performance reviews, salary negotiations, or difficult feedback sessions before having the real conversation. The AI can adjust the difficulty and realism based on your needs, giving you increasingly challenging scenarios as you improve.

## Technical Considerations for Enterprise Implementation

### Context Window Management in Practice

When implementing MCP in an enterprise setting, you need to understand the computational implications of large context windows. Bigger context windows require more compute power and GPU resources. If you're running local models, you'll need substantial VRAM (video RAM) to handle large contexts effectively.

For example, while a model like Gemma 34B might support up to 128,000 tokens officially, your GPU might not be able to support that full context due to VRAM limitations. Setting high context values can significantly impact memory usage and processing speed.

There are optimizations available to help with this:

**Flash Attention:** This changes how the model computes attention by processing tokens in chunks with optimized GPU routines. It never stores the full matrix of complications in memory at the same time, leading to significant improvements in both memory usage and speed.

**K-Cache and V-Cache Optimizations:** These compress data so it takes up less room in VRAM. Lower quantization (like quant 4) provides better compression.

**Paged Cache:** This moves attention cache between your GPU (VRAM) and system RAM, sharing memory with your system. The downside is significantly slower performance than VRAM.

### Security Considerations

The larger the context window, the larger the attack surface. LLMs can be hacked through creative prompting that can jailbreak out of their protection systems. The longer a conversation is, the more it can forget what's in the middle (that U-curve we discussed), and the easier it will be for an attacker to hide malicious content that could bypass safety precautions.

## The Bigger Picture: Enterprise Agentic AI

So, I hope you can see now how this really is a big deal. There's a broader vision here than just enhancing a desktop application with some way to help me write code locally. This is really a gateway to building true agentic AI in the enterprise, in a professional setting. That is really cool stuff.

Some people are concerned about cognitive offloading—the observed phenomenon that humans actually kind of stop thinking or "fall asleep at the wheel." People are concerned right now: is AI just making us dumber? My feeling is AI is a mirror. To people who want to offload work and who want to be lazy, it will help you. To people who want to be more cognitively sharp and critical thinkers, it will help you do that too.

For example, if you want to preserve or strengthen your critical thinking, part of your custom instructions should be some version of the following: "I'm trying to stay a critical and sharp analytical thinker. Whenever you see opportunities in our conversations, please push my critical thinking ability." Now, AI will do it.

The Model Context Protocol isn't just about making your desktop applications smarter—it's about creating a professional, scalable architecture for agentic AI that can work across your entire organization. With its pluggable, discoverable, and composable nature, MCP provides the foundation for building AI agents that can actually get things done in the real world.

Where could AI go? Well, it's really a function of who can get unleashed. Right now, the primary limitation is the limits of human imagination. As we unleash and ignite and spark more humans' imaginations, the kinds of applications that are possible—they're unthinkable, not because they're technologically impossible, but because they never occur to us personally.

As Nobel Prize-winning economist Thomas Schelling said: "No matter how heroic a man's imagination, he could never think of that which would not occur to him." If you take as a premise that the imagination space is a function of what would occur to various individuals, then as we equip different individuals, what we can imagine collectively expands.

So check it out, get started, and as always, let me know in the comments what you build. And perhaps the most important thing you could do with this article is actually hit stop and do something that's already blown your mind.

---

## Article Metadata

**Topic:** context engineering

**Generated:** 2025-10-18 09:17:16

**Sources:**

1. [Why MCP really is a big deal | Model Context Protocol with Tim Berglund](https://www.youtube.com/watch?v=FLpS7OfD5-s)
   - Channel: Confluent Developer
   - Views: 574,079
   - Comments: 739

2. [Stanford's Practical Guide to 10x Your AI Productivity | Jeremy Utley](https://www.youtube.com/watch?v=yMOmmnjy3sE)
   - Channel: EO
   - Views: 398,075
   - Comments: 425

3. [Why LLMs get dumb (Context Windows Explained)](https://www.youtube.com/watch?v=TeQDr4DkLYo)
   - Channel: NetworkChuck
   - Views: 151,817
   - Comments: 319

**Cost Summary:**

- Total Input Tokens: 21,695
- Total Output Tokens: 13,002
- Total Tokens: 34,697
- **Total Cost: $0.2601**
- Model: Claude Sonnet 4

