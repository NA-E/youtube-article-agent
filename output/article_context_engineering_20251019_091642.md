# Why Model Context Protocol (MCP) Really is a Big Deal

Model. Context. Protocol. It really is a big deal, but I think most people are missing the point here. Everybody's talking about enhancing desktop applications with agentic functionality. But if you want to write agentic AI applications at work like a professional, you're going to need a broader vision.

In order for me to give you that vision, I'm going to need to explain to you how it works. And here's a hint: comparing it to the USB-C of AI applications is probably not going to be helpful. Didn't help me, I don't think it's going to help you.

## Understanding the Core Problem: The Context Challenge

Now, let's start by remembering how an LLM basically works from an outside perspective, right? You have a prompt and you send that into an LLM. Out of that LLM, you get a response. Now, there are two problems here.

That response is just words. And if words are what you want, you're doing fine. But what if you want to do something? That's what agentic AI is all about. You want to cause effects out in the world. The AI needs to be able to take those actions or invoke what we call tools.

It also needs more up-to-date information or maybe just broader information than what's available in that core foundation model. And that's great. This guy is here as an API out on the internet. You might have wrapped that with the so-called Retrieval Augmented Generation pattern. Some people say RAG is old and busted and yesterday's news. In fact, in enterprise context, you may well be using this pattern and there's not a thing in the world wrong with that to bring the data of the enterprise into the context that the LLM can work with.

But here's something crucial to understand: LLMs are kind of like us, you and me, in that they have memories. Short-term memory, which means they can remember things. That's awesome. But also, sometimes they can forget stuff. And it happens like this. Let's say you and me, we're having some coffee and we're talking for about 15 minutes. In that short amount of time, we remember pretty much everything. I remember that story you told. You remember that dumb joke I said, but you're pretty fun to talk to. So, we end up talking for an hour, 2 hours, 3 hours, and at that point, it's kind of hard to keep track of stuff. I forget that amazing point you made. Thankfully, you forgot that dumb thing I said. And sometimes we forget the entire point of the conversation.

ChatGPT does the same thing. It's like you and your wife. The longer that conversation goes on, the more things you say, the more things it says back to you. It has to store all of that in its short-term memory. And that short-term memory has a limit. That limit is its context window.

### The Context Window Reality

Whether RAG is there or not doesn't really matter. The fact is there are going to be other resources in our world that we're going to need to get into the prompt, into the scope of what the model can deal with. And these can be anything:

- Files
- Binaries
- Databases
- Things happening in a Kafka topic (that's even a pretty likely source of resources)

So there's just this data out in the world that the agent needs to be aware of. These are two things that are just not going to be present in the base foundation model.

But here's the catch: all of this information takes up tokens in the context window. Tokens are how an AI counts the words you say to it. A sentence might be 133 characters or 26 words, but an LLM might see it as 38 tokens. And right now, different models have different context limits:

- GPT-4o: 128,000 tokens
- Claude 3.5: 200,000 tokens  
- Gemini 2.5: 1 million tokens
- Some newer models are pushing toward 2 million tokens

But even if you have a super large context window, it doesn't mean the LLM won't kind of freak out and forget stuff, become less accurate, or start to go extremely slow. There was a paper released called "Lost in the Middle" that showed us how LLMs are kind of like us with paying attention. Just like watching a long movie, they'll pay attention to the first part, then zone out in the middle, and wake up at the end. The models were more accurate with info at the beginning and even with info at the end, but in the middle, huge drop off. And across the board, we saw this U shape.

This is where MCP becomes crucial—it's not just about cramming everything into one massive context window. It's about intelligently managing what information gets included and when.

## The Context Engineering Foundation

Before diving deeper into MCP's architecture, it's crucial to understand that building effective agentic AI applications isn't just about the protocol—it's about understanding how to work with AI as a collaborative partner. AI is bad software but it's good people. When I realize that I'm dealing with a good person but a bad software, then it changes how I approach it and I ask for volume and I iterate and I ask it to try again and I ask it to reconsider.

The people who are the best users of AI are not coders, they're coaches. They aren't developers or software engineers. They're teachers and mentors and people who have learned to get exceptional output out of other intelligences.

This mindset becomes essential when working with MCP because you're not just connecting systems—you're orchestrating intelligent collaboration between your agent and various data sources and tools. AI wants to be helpful and so it's predisposed to say yes. It's a super eager, super enthusiastic intern who's tireless, who's capable, who will do a bunch of work, but they're not really great at pushing back.

## The MCP Architecture

Now, let's talk about a little bit of architecture. What we're doing is building an agent. You could think of it as a microservice. There's nothing particularly exotic about this. But, in MCP terms, this is called the host application. And the host application uses the MCP client library to create an instance of a client in there.

Out here, we're going to create an MCP server. This may be a server that already exists that somebody else has built that we want to take advantage of to bring agentic functionality into our service, or this could be a server that we ourselves are creating.

Inside the server, what do we have? Well, we've got access to tools, resources, prompts, capabilities that the server makes available and even describes to the outside world. So, this is a server process. There's a URL, port, etc, and a variety of well-known RESTful endpoints described by the MCP specification that are implemented by this server, including this capabilities list that tells the world, tells the host application, tells the client, whether there are tools present, what sort of resources might be available, what prompts it has, etc, etc.

### Connection Options

The connection between these two things, between client and server, can be two things:

1. **Standard IO**: Interestingly, this can be standard IO. So if this is a process running locally on my laptop and I've got some LLM host application, like say, Claude Desktop or something, that's something that shows up in a lot of the examples, they can just communicate via pipes and standard IO. We don't want that. That's not kind of what we're interested in in the model I'm trying to give you here.

2. **HTTP and Server Sent Events**: So, we also have as an option HTTP and Server Sent Events, and the messages being exchanged here are going to be in JSON RPC.

Now, I will not apologize for those technology choices because I didn't make them. Yes, they have raised the occasional eyebrow, but this is what we've got. There's a little bit of sort of protocol for a client announcing itself to the server and then establishing communications. There are ways for servers to send asynchronous notifications back to the client. We'll come back to that in a minute. So, a relatively rich setup here for client and server to talk.

## A Real-World Example: Appointment Scheduling

But what does it do? Let's walk through an example. I think that would be helpful. Let's say we're building a service for making appointments. Sort of generalized meet with somebody, some group of people at some place, and not necessarily a conference room in the office, but maybe we're getting coffee. Maybe we're getting breakfast. Maybe it's a romantic dinner with your spouse.

I've just described a number of tools and resources that are necessary to make that happen. Let's think about that:

**Tools needed:**
- Create a calendar invite
- Calendar API integration
- Making a reservation at a restaurant

**Resources needed:**
- See when my calendar is free
- Maybe access to the counterparty's calendar (depending on permissions)
- Places I might meet
- Knowing what restaurants, what coffee shops, what breakfast joints are in the area

These are resources that I wanna make available to my agentic application. I could just do all that stuff, do the calendar integration, go talk to Yelp or whatever APIs I wanna do and bake that into my agent, but then it's locked there and nobody else can get at that unless they've got that code. So the whole idea of MCP is I'm putting those things in here.

## The MCP Workflow in Action

Let's go through a workflow of how this might work. A prompt comes in, and that prompt from the user and that's the actual input and it's something like, "I wanna have coffee with Peter next week."

Okay, well, you just ask the LLM, it's like, "Who's Peter? Where's coffee? I can't help you with this." But here we can start to do better.

### Step 1: Capability Discovery

This application, the host, the client, whatever you wanna call it, can say, "What capabilities do you have?" It knows the URL of this agent. You've had to tell it and maybe very tactically there's a properties file somewhere with a little list of the URLs of servers that are registered with the agent. And so it can interrogate the capabilities and see, "Oh, you have resources. Okay. Let me get a list of your resources" which will include text descriptions of each resource. And it's important when writing the server, when building a server to make those good.

### Step 2: Resource Evaluation with Chain of Thought

I can take my prompt. I don't know, I'm just a poor little agentic application. I don't know how to figure out from the input whether I need any of those resources, but I can ask my model. I can say, "You know what, on pass number one, I'll say, here is what my user said. Here is a list of resources: resource one, resource two, resource three. Do I need these?"

This is where understanding chain of thought reasoning becomes crucial. When you get an AI to think out loud, so to speak, it meaningfully improves the outputs of the model. So instead of just asking "Do I need these resources?", you'd say: "Before you respond to my query, please walk me through your thought process step by step. Here is what my user said. Here is a list of resources. Do I need these and why?"

We are telling the LLM, "I got this request. I have things like this. Do you think I should go get anything from them?" We submit this as a prompt up to our LLM and it tells us in return, "Yes, you need resource two. That resource two, that list of coffee shops in the area, that looks super interesting. Please give me that."

### Step 3: Resource Retrieval and Processing

And so now my client says, "Oh, resource two? I know where that is. I'll just go ask my MCP server for the details of resource two." Maybe passing some parameters, maybe not. And then I will get that text back or whatever that data is. I'll get that back and serialize it as text or otherwise attach it to my next prompt.

Where I say, again, "Here is my user prompt. And now here is the resource data." And I provide that data in detail and then ask, "What should I do as a result?" That's how I get the model to help me interpret the resources.

### Step 4: Tool Invocation with Reverse Prompting

How do I interpret the tools? Well, the good news is, so this call is gonna go back to that same LLM and the APIs now for the foundation models, the biggies, I can actually put the description of the tools in the API call. I don't even have to mess with the prompt or anything. It's structured data that goes in there, the name of the tool, the URL, the schema of the parameters, all that. And in the reply, that tells me if there's a tool I should invoke, it'll say, "Yes, invoke this tool, pass these parameters."

But here's where reverse prompting becomes valuable. Instead of having the AI guess what parameters to use, you can ask it to request the information it needs: "Before you invoke any tools, ask me for any information you need to do a good job." The model will first walk you through its thought process and then instead of making assumptions, it'll say, "I'm going to need Peter's email address and your preferred time range to be able to create this calendar invite."

I don't have to write any of the code to parse any of the stuff out because I don't know how to do that. That's all very difficult stuff that LLMs are wonderful at. And those APIs will help me with that tool invocation. They won't call them, okay? ChatGPT, Claude, Gemini, they're not gonna go invoke some URL inside my network and go do something. You know, that's a little bit Skynet-y there, right? But they're gonna tell me, "I recommend you do this." And now my client code gets to make the decision, maybe asking the user first, maybe not, to go call that tool and cause the effect out in the world.

## Managing Context Windows in MCP Applications

Here's where understanding context windows becomes crucial for MCP applications. When you're orchestrating multiple MCP servers, each providing resources and tools, you need to be strategic about what goes into your context window and when.

A quick solution, and this is a rule I try to go by when I'm talking with LLMs: when you change an idea, when it's a significant shift from what you're currently talking about, start a new chat. The performance will be so much better. In fact, when sometimes when you're talking with other LLMs like Claude, it'll even tell you at the bottom, "Hey, you've been talking for a minute, things are going to slow down. Why don't you go and start a new chat so things can be better?"

In MCP applications, this translates to being smart about context management:

1. **Selective Resource Loading**: Don't load all available resources at once. Use the discovery phase to determine what's actually needed.
2. **Context Chunking**: Break complex workflows into discrete steps, each with its own focused context.
3. **Resource Summarization**: Instead of dumping raw data into the context, have your MCP servers provide summarized or filtered views of resources.

## The Power of MCP: Key Benefits

So you can kind of see how this works. So instead of just baking all this code in here, we have this that is now pluggable and discoverable. I don't need to know very much about what this tool does. I just plug it in. I just say, "Hey, you have this agent registered with you, go find out about it, go through this process, and you get its functionality."

### 1. Pluggability
You can connect different MCP servers without hardcoding functionality into your agent.

### 2. Discoverability
Agents can automatically discover what capabilities are available through the MCP protocol.

### 3. Composability
They're also composable. The server itself can be a client. So, let's say I had some data source that I knew was in Kafka out there, and I don't wanna go write a bunch of extra Kafka code to go do that in here. Well, I can just then go use, let's say the Confluent MCP server and connect to that topic or even do actually a bunch more stuff. It's a pretty cool MCP server. If Kafka and Confluent are a part of your life, it's good stuff.

But if I just need to consume from a Kafka topic, this server itself gets to be a client of another server. So I've got pluggability, discoverability, composability, huge benefits. These are things that we want in our code.

## Building Effective MCP Applications: The Human Element

Understanding MCP's technical architecture is only half the battle. The other half is understanding how to effectively collaborate with AI systems within this framework. This is where the mindset shift from treating AI as software to treating it as a collaborative partner becomes crucial.

### Context Engineering in MCP

Context engineering is just prompt engineering on steroids. It's basically saying, what are all of the things that I need to give to an AI in order for it to perform the task that I'm asking for it? In the context of MCP, this becomes even more important because you're not just crafting prompts—you're orchestrating the entire flow of information between your agent, various MCP servers, and the AI model.

For example, when your MCP server returns resource data, you need to think about:
- How to present that data to the AI in a way that's most useful
- What context about the data source the AI needs to understand
- How to structure the information so the AI can reason about it effectively

All of the stuff that are implicit, you actually have to make explicit. And the simplest test for context engineering is actually the test of humanity. Write down your prompt and whatever documentation you provide to an AI and then walk down the hall and give it to a human colleague. If they cannot do the thing you're asking for, you shouldn't be surprised that AI can't do it.

### Role Assignment in MCP Workflows

Assigning a role is one of the most foundational techniques that you can leverage because it's effectively telling the AI where in its knowledge it should focus. In MCP applications, this becomes particularly powerful because you can assign different roles for different phases of the workflow:

- When evaluating resources: "You are a data analyst helping me determine which resources are relevant for this task."
- When interpreting tool responses: "You are a system integration expert helping me understand what this API response means for my user's request."
- When making decisions about tool invocation: "You are a careful project manager who always asks for clarification before taking action."

Each of those titles triggers all sorts of deep associations with knowledge on the internet, helping the AI focus on the most relevant expertise for each phase of your MCP workflow.

## Advanced MCP Patterns: Learning from AI Collaboration

### The Flight Simulator Approach

Just as you can use AI to practice difficult conversations, you can use MCP to create sophisticated testing and validation environments for your agentic applications. Imagine setting up MCP servers that simulate various enterprise systems—databases that return test data, APIs that simulate different response conditions, tools that log actions without actually executing them.

This lets you test your agent's decision-making process in a controlled environment before connecting to real systems. You can even have one MCP server simulate error conditions while another provides the "happy path" responses, letting you validate how your agent handles different scenarios.

### Multi-Agent MCP Architectures

The composability of MCP opens up fascinating possibilities for multi-agent systems. You could have:

- A **coordinator agent** that uses MCP to discover and orchestrate other agents
- **Specialist agents** that each expose their capabilities through MCP servers
- **Feedback agents** that monitor the interactions and provide optimization suggestions

This mirrors the pattern of having different AI assistants for different roles—one for personality profiling, one for playing a character, and one for providing feedback—but now these can be persistent, discoverable services that multiple applications can leverage.

## The Technical Reality: Performance and Security Considerations

When you're building MCP applications, especially ones that handle large amounts of data or complex workflows, you need to understand the computational realities. Every time you add to that conversation, that math problem that has to run to figure out what's important gets bigger and it requires more GPU power. And that is why in those larger conversations, the LLM starts to hallucinate and it seems just a bit more slow. It's using a ton of memory and it's having to do some crazy math every time you talk to it.

This has implications for MCP design:

1. **Resource Optimization**: Design your MCP servers to provide focused, relevant data rather than comprehensive dumps
2. **Caching Strategies**: Implement intelligent caching to avoid redundant resource fetches
3. **Context Pruning**: Build mechanisms to remove irrelevant context as conversations evolve

### Security Implications

The larger attack surface is a real concern. LLMs can be hacked and they're vulnerable to some creative prompting that can jailbreak out of their protection systems. The longer a conversation is, the more it can kind of like forget what's in the middle, as we saw in that little U curve, and the easier it will be for an attacker to hide some malicious stuff in there that could bypass its safety precautions.

For MCP applications, this means:
- Validate and sanitize all data coming from MCP servers
- Implement proper authentication and authorization between MCP clients and servers
- Monitor for unusual patterns in resource requests or tool invocations
- Consider implementing conversation reset policies for long-running agents

## The Enterprise Reality: Why MCP Matters Now

Right now, the primary limitation is the limits of human imagination. And as we unleash and ignite and spark more humans imaginations, the kinds of applications that are possible or they're unthinkable, not because they're technologically impossible, but because they never occur to us personally.

This is exactly why MCP is such a big deal in enterprise contexts. It's not just about the protocol—it's about creating an ecosystem where:

1. **Domain experts** can expose their knowledge and tools through MCP servers without needing to understand AI development
2. **AI developers** can build sophisticated agents without needing to understand every business domain
3. **Organizations** can create reusable, discoverable AI capabilities that compound over time

### The Network Effect

As more teams within an organization create MCP servers, the value for everyone increases exponentially. The marketing team's customer data MCP server becomes valuable to sales. The engineering team's deployment status MCP server becomes valuable to customer success. The finance team's budget tracking MCP server becomes valuable to project management.

This creates what innovation studies has called the adjacent possible for a long time. What is possible is just adjacent to what is. And as we increase adoption and increase fluency and competency and increasingly mastery of AI collaboration through MCP, then we're increasing the adjacent possible.

## The Broader Vision

So, I hope you can see now how this really is a big deal. There's a broader vision here than just enhancing a desktop application with some way to help me write code locally. This is really a gateway to building true agentic AI in the enterprise, in a professional setting. That is really cool stuff.

Model Context Protocol isn't just about making your desktop apps a little smarter—it's about creating a standardized way for AI agents to interact with the vast array of tools and data sources that exist in professional environments. It's about building systems that can discover, connect to, and leverage capabilities without hardcoding every integration.

But more than that, MCP represents a fundamental shift in how we think about AI collaboration. It's moving us from a world where we build monolithic AI applications to one where we create ecosystems of intelligent, composable services. It's the difference between having a single, smart assistant and having access to a network of specialized experts who can collaborate seamlessly.

When you understand MCP this way—not just as a protocol, but as an enabler of organizational AI intelligence—you realize we're not just talking about better software architecture. We're talking about the foundation for enterprise-grade agentic AI that can actually get work done in the real world, learn from human expertise, and continuously expand its capabilities through the collective intelligence of the organization.

The most important thing you could do is actually stop reading and start implementing. Because as we equip different individuals with these capabilities, what we can imagine collectively expands. And that's where the real power of MCP will be realized—not in the protocol itself, but in the explosion of creativity and capability that emerges when intelligent humans and intelligent systems can truly collaborate.

Just remember: when you're building these systems, respect the context window limits, design for performance, and always keep security in mind. Because at the end of the day, MCP is about creating sustainable, scalable AI collaboration—and that means building systems that work well not just in demos, but in the messy, complex reality of actual work.

---

## Article Metadata

**Topic:** context engineering

**Generated:** 2025-10-19 09:16:42

**Sources:**

1. [Why MCP really is a big deal | Model Context Protocol with Tim Berglund](https://www.youtube.com/watch?v=FLpS7OfD5-s)
   - Channel: Confluent Developer
   - Views: 575,378
   - Comments: 739

2. [Stanford's Practical Guide to 10x Your AI Productivity | Jeremy Utley](https://www.youtube.com/watch?v=yMOmmnjy3sE)
   - Channel: EO
   - Views: 399,431
   - Comments: 426

3. [Why LLMs get dumb (Context Windows Explained)](https://www.youtube.com/watch?v=TeQDr4DkLYo)
   - Channel: NetworkChuck
   - Views: 152,042
   - Comments: 318

**Cost Summary:**

- Total Input Tokens: 21,530
- Total Output Tokens: 12,725
- Total Tokens: 34,255
- **Total Cost: $0.2555**
- Model: Claude Sonnet 4

