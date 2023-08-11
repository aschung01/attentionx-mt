from base import promptlabs


def start_game(characters: str):
    output, log = promptlabs.pipeline(pipeline_name="Mystery_game").run(
        inputs={"characters": characters}
    )
    settings = {
        "characters": characters,
        "places": log.chain_outputs[0].output_variables["places"],
        "tools": log.chain_outputs[0].output_variables["tools"],
        "story": log.chain_outputs[1].output_variables["story"],
        "answer": log.chain_outputs[1].output_variables["answer"],
        "explanation": log.chain_outputs[1].output_variables["explanation"],
    }
    return settings

