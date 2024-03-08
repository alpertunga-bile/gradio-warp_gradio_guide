"""gr.SimpleImage() component."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from gradio_client.documentation import document

from gradio.components.base import Component
from gradio.data_classes import FileData
from gradio.events import Events


@document()
class SimpleImage(Component):
    """
    Creates an image component that can be used to upload images (as an input) or display images (as an output).
    """

    EVENTS = [
        Events.clear,
        Events.change,
        Events.upload,
    ]

    data_model = FileData

    def __init__(
        self,
        value: str | None = None,
        *,
        label: str | None = None,
        every: float | None = None,
        show_label: bool | None = None,
        show_download_button: bool = True,
        container: bool = True,
        scale: int | None = None,
        min_width: int = 160,
        interactive: bool | None = None,
        visible: bool = True,
        elem_id: str | None = None,
        elem_classes: list[str] | str | None = None,
        render: bool = True,
    ):
        """
        Parameters:
            value: A path or URL for the default value that SimpleImage component is going to take. If callable, the function will be called whenever the app loads to set the initial value of the component.
            label: The label for this component. Appears above the component and is also used as the header if there are a table of examples for this component. If None and used in a `gr.Interface`, the label will be the name of the parameter this component is assigned to.
            every: If `value` is a callable, run the function 'every' number of seconds while the client connection is open. Has no effect otherwise. Queue must be enabled. The event can be accessed (e.g. to cancel it) via this component's .load_event attribute.
            show_label: if True, will display label.
            show_download_button: If True, will display button to download image.
            container: If True, will place the component in a container - providing some extra padding around the border.
            scale: relative size compared to adjacent Components. For example if Components A and B are in a Row, and A has scale=2, and B has scale=1, A will be twice as wide as B. Should be an integer. scale applies in Rows, and to top-level Components in Blocks where fill_height=True.
            min_width: minimum pixel width, will wrap if not sufficient screen space to satisfy this value. If a certain scale value results in this Component being narrower than min_width, the min_width parameter will be respected first.
            interactive: if True, will allow users to upload and edit an image; if False, can only be used to display images. If not provided, this is inferred based on whether the component is used as an input or output.
            visible: If False, component will be hidden.
            elem_id: An optional string that is assigned as the id of this component in the HTML DOM. Can be used for targeting CSS styles.
            elem_classes: An optional list of strings that are assigned as the classes of this component in the HTML DOM. Can be used for targeting CSS styles.
            render: If False, component will not render be rendered in the Blocks context. Should be used if the intention is to assign event listeners now but render the component later.
        """
        self.show_download_button = show_download_button
        super().__init__(
            label=label,
            every=every,
            show_label=show_label,
            container=container,
            scale=scale,
            min_width=min_width,
            interactive=interactive,
            visible=visible,
            elem_id=elem_id,
            elem_classes=elem_classes,
            render=render,
            value=value,
        )

    def preprocess(self, payload: FileData | None) -> str | None:
        """
        Parameters:
            payload: A FileData object containing the image data.
        Returns:
            A `str` containing the path to the image.
        """
        if payload is None:
            return None
        return payload.path

    def postprocess(self, value: str | Path | None) -> FileData | None:
        """
        Parameters:
            value: Expects a `str` or `pathlib.Path` object containing the path to the image.
        Returns:
            A FileData object containing the image data.
        """
        if value is None:
            return None
        return FileData(path=str(value), orig_name=Path(value).name)

    def example_payload(self) -> Any:
        return "https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png"

    def example_value(self) -> Any:
        return "https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png"
