import os
import openai
from dotenv import load_dotenv
from typing import Union, List

if os.path.exists(".env"):
    load_dotenv()
    
openai.organization = "org-JXuF0c8m0LBGctd5KgIg1BN1"
openai.api_key = os.getenv("OPENAI_API_KEY")

BABBAGE = "text-babbage-001"  # Cheapest model that works, use to test if code is working
CURIE = "text-curie-001"  # Better model, use to experiment with API
DAVINCI = "text-davinci-003"  # Best mode, use for finalization and user product


def list_models():
    """
    Prints a list of all OpenAI models available through their API

    Most of the models that are not listed in the official documentation return none-sense
    """
    models_list = openai.Model.list()
    for model in models_list.data:
        print(model.id)


def get_model_info(model_name):
    """
    Prints information about a model retrieved from OpenAI API

    :param model_name: name of the model to fetch info for
    """
    model_info = openai.Model.retrieve(model_name)
    print(model_info)


def text_completion(
        prompt: Union[str, List[str]],
        model: str = BABBAGE,
        max_tokens: int = 16,
        temperature: float = 0,
        top_p: float = 1,
        presence_penalty: float = 0,
        frequency_penalty: float = 0,
        n=1,
        stream=False,
        logprobs: int = None,
        stop: Union[str, List[str]] = None, ):
    """
    Calls GPT-3 completion API

    Models
            BABBAGE:    cheapest model that works, use to test if code is working
            CURIE:      better model, use to experiment with API
            DAVINCI:    best mode, use for finalization and user product

    :param prompt: The prompt(s) to generate completions for, encoded as a string, array of strings,
        array of tokens, or array of token arrays.
    :param model: ID of the model to use.
    :param max_tokens: The maximum number of tokens to generate in the completion. The token
        count of your prompt plus max_tokens cannot exceed the model's context
        length.
    :param temperature:What sampling temperature to use. Higher values means the model will take
        more risks. Try 0.9 for more creative applications, and 0 (argmax sampling) for ones with a
        well-defined answer.
    :param top_p: An alternative to sampling with temperature, called nucleus sampling, where the
        model considers the results of the tokens with top_p probability mass. So 0.1 means only the
        tokens comprising the top 10% probability mass are considered. We generally recommend
        altering this or temperature but not both.
    :param presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens
        based on whether they appear in the text so far, increasing the model's likelihood to
        talk about new topics.
    :param frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens
        based on their existing frequency in the text so far, decreasing the model's likelihood
        to repeat the same line verbatim.
    :param n: How many completions to generate for each prompt.
    :param stream:Whether to stream back partial progress. If set, tokens will be sent as
        data-only  server-sent events as they become available, with the stream terminated by a
        data: [DONE] message.
    :param logprobs:Include the log probabilities on the logprobs most likely tokens, as well
        the chosen tokens. For example, if logprobs is 5, the API will return a list of the 5 most
        likely tokens
    :param stop: Up to 4 sequences where the API will stop generating further tokens. The
        returned text will not contain the stop sequence.

    :returns: the result of the text completion request
    """
    result = openai.Completion.create(
        model=model,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature,
        presence_penalty=presence_penalty,
        frequency_penalty=frequency_penalty,
        top_p=top_p,
        n=n,
        stream=stream,
        logprobs=logprobs,
        stop=stop,
    )
    return result


def get_cover_letter_prompt(resume: str, job_posting: str, past_experiences: str = None):
    past_experiences_string = f'\n\nPast Experiences:\n{past_experiences}'
    prompt = f"You are a career advisor. " \
             f"You have been helping people land life changing jobs for the past 20 years. " \
             f"You are tasked with helping candidates writes cover letters for jobs they are " \
             f"applying to. You will be given a job posting, " \
             f"{'a collection of past experiences, ' if past_experiences else ''}" \
             f"and a resume. You will produce a cover letter that is based on the resume, " \
             f"{'the past experiences, ' if past_experiences else ''}" \
             f"and the job posting. Do not include experiences from projects that are not " \
             f"mentioned in the resume." \
             f"\n\nResume:\n{resume}" \
             f"{past_experiences_string if past_experiences else ''}" \
             f"\n\nJob Posting:\n{job_posting}" \
             f"\n\nCover Letter:\n"
    return prompt


def generate_cover_letter(resume: str, job_posting: str, past_experiences: str = None):
    if not resume or len(resume) > 700:
        print("bad resume")
        return
    if not job_posting or len(job_posting) > 700:
        print("bad job_posting")
        return
    if past_experiences and len(past_experiences) > 700:
        print("bad past_experiences")
        return

    prompt = get_cover_letter_prompt(resume, job_posting, past_experiences)
    result = text_completion(
        prompt=prompt,
        model=DAVINCI,
        max_tokens=1500,
        temperature=0.5,
        presence_penalty=0.75,
        frequency_penalty=0.75
    )
    print("Cover Letter Generated")
    return result.choices[0].text
