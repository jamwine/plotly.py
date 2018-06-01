import _plotly_utils.basevalidators


class ArrayminussrcValidator(_plotly_utils.basevalidators.StringValidator):

    def __init__(
        self,
        plotly_name='arrayminussrc',
        parent_name='scattergl.error_y',
        **kwargs
    ):
        super(ArrayminussrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='none',
            role='info',
            **kwargs
        )