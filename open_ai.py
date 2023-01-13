import os
import openai
from dotenv import load_dotenv
from typing import Union

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
        prompt: Union[str, list[str]],
        model=BABBAGE,
        max_tokens=16,
        temperature=0,
        n=1,
        stream=False,
        logprobs: int = None,
        stop: Union[str, list[str]] = None, ):
    """
    Calls GPT-3 completion API

    Models
            BABBAGE:    cheapest model that works, use to test if code is working
            CURIE:      better model, use to experiment with API
            DAVINCI:    best mode, use for finalization and user product

    :param prompt: The prompt(s) to generate completions for, encoded as a string, array of strings,
        array of tokens, or array of token arrays.
    :param max_tokens: The maximum number of tokens to generate in the completion. The token
        count of your prompt plus max_tokens cannot exceed the model's context
        length.
    :param temperature:What sampling temperature to use. Higher values means the model will take
        more risks. Try 0.9 for more creative applications, and 0 (argmax sampling) for ones with a
        well-defined answer.
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
        n=n,
        stream=stream,
        logprobs=logprobs,
        stop=stop,
    )
    return result
