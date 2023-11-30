import click
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from cliaiai.tools import file_or_stdout
from cliaiai import translate as translate_service, command as command_service


@click.group()
@click.option('--output', help='where to write result, if not provided will write to stdout')
@click.pass_context
def main(ctx, output):
    pass


@click.argument("text")
@main.command(help='translate text')
@click.pass_context
def translate(ctx: click.Context, text: str):
    output_path = ctx.parent.params['output']

    translations = translate_service.execute(text)
    result = inquirer.select(
        message="Which translation fits you the best?",
        choices=[
            Choice(
                value=t['translation'],
                name=f"{t['translation']} (from: {t['source_language']} to: {t['target_language']})",

            ) for t in translations
        ],
    ).execute()

    with file_or_stdout(output_path) as outfile:
        click.echo(result, file=outfile)


@click.argument("text")
@main.command(help="generate some cli commands to perform task")
@click.pass_context
def command(ctx: click.Context, text: str):
    output_path = ctx.parent.params['output']

    notes, solutions = command_service.execute(text)

    click.echo(f"\nNote: {notes}\n\n")

    result = inquirer.select(
        message="Which command fits you the best?",
        choices=[
            Choice(
                value=solution['command'],
                name=f"`{solution['command']}` - {solution['comment']}",
            ) for solution in solutions
        ],
    ).execute()

    with file_or_stdout(output_path) as outfile:
        click.echo(result, file=outfile)


@click.option('--input', help='diff file')
@click.option('--output', help='where to write result, if not provided will write to stdout')
@main.command(help="give opinion about diff")
@click.pass_context
def diff(ctx, input, output):
    raise NotImplementedError('work in progress')


if __name__ == "__main__":
    main()
