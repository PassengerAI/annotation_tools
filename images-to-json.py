import click

from annotation_tools.converter import from_images


@click.command()
@click.argument('images_path', type=click.Path(exists=True, file_okay=False,
                                               resolve_path=True))
@click.argument('output_file',
                type=click.Path(dir_okay=True, resolve_path=True))
def images_to_json(images_path, output_file):
    """Convert a list of image files to a json, to be used for loading to
    Visipedia."""
    from_images(images_path, output_file)


if __name__ == '__main__':
    images_to_json()
