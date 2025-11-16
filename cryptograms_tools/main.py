import click
from cryptograms_tools.core.cyphers import cyphers, available_cyphers


@click.command()
@click.option(
    "--cypher",
    "-c",
    type=click.Choice(available_cyphers),
    required=True,
    help="The cypher text to decrypt.",
)
@click.option("--key", "-k", required=True, help="The key to use for decryption.")
@click.option(
    "--side",
    "-s",
    type=click.Choice(["encrypt", "decrypt"]),
    required=True,
    help="Whether to encrypt or decrypt the input.",
)
@click.option("--input", "-i", required=True, help="The input string to process.")
def main(cypher: str, key: str, side: str, input: str):
    input_bytes = input.encode("utf-8")
    if side == "encrypt":
        result_bytes = cyphers[cypher].encrypt(input_bytes, key)
    else:
        result_bytes = cyphers[cypher].decrypt(input_bytes, key)
    result = result_bytes.decode("utf-8", errors="ignore")
    click.echo(result)
