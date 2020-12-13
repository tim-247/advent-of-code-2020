from parsimonious.grammar import Grammar, NodeVisitor
import networkx as nx


with open("day7/input", "r") as input:
    inputlines = input.readlines()

grammar = Grammar(r"""
    LINE = (ENTRY / TERMINAL)

    TERMINAL = PARENT "no other bags." "\n"?
    ENTRY = PARENT CHILDREN "." "\n"?

    PARENT = COLOR " bags contain "
    CHILDREN = CHILD+
    CHILD = NUMBER " " COLOR " " BAGBAGS SEPARATOR

    NUMBER = ~r"\d+"
    COLOR = ~r"\w+ \w+"
    BAGBAGS = ("bags" / "bag")
    SEPARATOR = ~r"(, |(?=\.))"
""")


class LineInspector(NodeVisitor):
    def visit_ENTRY(self, node, visited_children):
        parent, children, *_ = visited_children
        return {"parent": parent, "children": children}

    def visit_PARENT(self, node, visited_children):
        return visited_children[0]

    def visit_CHILD(self, node, visited_children):
        return (visited_children[0], visited_children[2])

    def visit_COLOR(self, node, visited_children):
        return node.text

    def visit_TERMINAL(self, node, visited_children):
        parent, *_ = visited_children
        return {"parent": parent, "children": []}
    
    def visit_NUMBER(self, node, visited_children):
        return int(node.text)

    def generic_visit(self, node, visited_children):
        return visited_children or node


li = LineInspector()
li.grammar = grammar

tree = nx.DiGraph()
for line in inputlines:
    bags = li.parse(line)[0]
    tree.add_node(bags['parent'])
    tree.add_nodes_from(bags['children'])
    for count, child in bags['children']:
        tree.add_edge(bags['parent'], child, count=count)

def get_count(parent):
    count = 0
    for child in tree.neighbors(parent):
        count += get_count(child) * tree.edges[parent, child]["count"]
    return 1 + count

print(get_count("shiny gold") - 1)
