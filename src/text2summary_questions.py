import os
import openai

import ast

EXAMPLE_TEXT = """
Let’s practice identifying functional groups in different compounds. So this molecule on the left is found in perfumes. And let’s look for some of the functional groups that we’ve talked about in the previous videos. Well here is a carbon-carbon double bond. And we know that a carbon-carbon double bond is an alkene. So here is an alkene-functional group. Here’s another alkene. Right? Here’s another carbon-carbon double bond. What is this functional group? We have an OH, and then we have the rest of the molecule. So we have RoH. RoH is an alcohol. So there’s also an alcohol present in this compound. Next let’s look at aspirin. So what functional groups can we find in aspirin? Well here is an aromatic ring. All right? So this is an aereen. So there’s an aereen functional group present in aspirin. What about this one up here? We have an OH, and the oxygen is directly bonded to a carbonyl. So let’s go ahead and write that out. We have an OH, where the oxygen is directly bonded to a carbon, double bonded to an oxygen, and then we have the rest of the molecule. So hopefully you recognize this as being a carboxylic acid. So let me go ahead and write that out here. So this is a carboxylic acid. All right. So we have our next functional group. We have an oxygen, and then oxygen is directly bonded to a carbonyl. All right? So here’s a carbon double bonded to an oxygen. So let’s write this out. We have an oxygen directly bonded to a carbonyl. And then for this oxygen we have the rest of the molecules. That’s all of this stuff over here. And then on the other side of the carbonyl we have another R group. So I’ll go ahead and write that in. So that is an ester. R-O-C double bond O-R is an ester. So there’s an ester functional group present in the aspirin molecule. Let’s look at some of the common mistakes that students make. One of them is students will say a carboxylic acid is an alcohol. So let me write out here a carboxylic acid so we can talk about that. So sometimes the students will look at that and say, oh, well I see an OH and then I see the rest of the molecule. So isn’t that an alcohol? But since this oxygen is right next to this carbonyl, this is a carboxylic acid. So this is an example of a carboxylic acid. If we move the OH further away from the carbonyl, let’s go ahead and draw one out like that. So here is our carbonyl. And now the OH is moved further away. Now we do have an alcohol. Now we have an OH and then the rest of the molecule. So this would be, let me go and use a different color here. So now we are talking about an alcohol. So this is an alcohol. And what would this one be? We have a carbonyl and then we have an R group on one side and R group on the other side. That is a ketone. Let me draw this out. So when you have a carbonyl and an R group on one side and R group on the other side, they could be the same R group. They could be a different R group. Sometimes you’ll see like R prime drawn for that. So this is a ketone. So now we have a ketone and an alcohol.
"""

openai.api_key = os.environ['OPENAI_API_KEY']

def generate_summary(text:str, nSentences = 3): 
    '''Returns a dict of a summary of nSentences of the text'''

    messages = [{"role": "system", "content": "You are a helpful assistant."}]

    message = f"Give a summary of '{text}' in {nSentences} sentences"
    
    messages.append(
            {"role": "user", "content": message},
    )
    chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
    )
    summary = chat_completion.choices[0].message.content

    return {'summary': summary}


def generate_truefalse_questions(text:str, nQuestions = 3):
    '''
    Generate true/false questions based on a text

    Returns:
    ---------
    questions_list: list of dict
        list of dict of lenght nQuestions with keys 'question', 'answer', 'reasoning'
        examples: [{'question': 'Is an alkene present in the perfume compound?', 'answer': 'True', 'reasoning': 'The text explicitly states that there are alkene functional groups present in the perfume molecule.'}, {'question': 'Is a carboxylic acid considered an alcohol?', 'answer': 'False', 'reasoning': 'Although a carboxylic acid contains an OH group, it is not considered an alcohol because the OH is bonded to a carbonyl group in a distinct functional group called a carboxylic acid. The text clarifies this common mistake made by students.'}]
    '''

    print('Generating {} True/False questions...'.format(nQuestions))
    messages = [{"role": "system", "content": "You are a helpful assistant."}]

    message = "Give me {} TRUE/FALSE questions for this text : '{}'. Format it in python dictionary QUESTION, ANSWER, REASONING.".format(nQuestions, text)
    
    messages.append(
            {"role": "user", "content": message},
    )
    chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
    )
    questions = chat_completion.choices[0].message.content

    questions_dict = ast.literal_eval(questions)

    questions_list = [values for values in questions_dict.values()]
    print(questions_list)

    return questions_list


