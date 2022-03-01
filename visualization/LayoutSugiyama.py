from .BnLayout import BnLayout, networkx_to_igraph


class LayoutSugiyama(BnLayout):
    """
    Sugiyama Layout class.
    """

    def __init__(self, graph, graph_initial_width=None,
                 graph_initial_height=None):
        """
        Sugiyama Layout class constructor.
        @param graph:
        @param graph_initial_width:
        @param graph_initial_height:
        """
        super(LayoutSugiyama, self).__init__(graph, graph_initial_width,
                                             graph_initial_height)

    def run(self):
        graph_igraph = networkx_to_igraph(self.graph)
        nodes = list(self.graph.nodes())

        self.layout = {}
        layout = graph_igraph.layout('sugiyama')
        for i, position in enumerate(layout):
            if i < len(nodes):
                self.layout[nodes[i]] = (position[0], position[1])

        return self.layout
