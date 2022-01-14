def create_main_subnet(alembic_input):
    subnet_node = hou.node('/obj').createNode('subnet', 'extract_animation')
    subnet_node.moveToGoodPosition()
    return subnet_node

def create_divide_into_parts_geo_node(parent_node):
    divide_geo_node = parent_node.createNode('geo', 'divide_into_parts')
    divide_geo_node.moveToGoodPosition()
    return divide_geo_node

def divide_into_parts(parent_node, alembic_path):
    obj_merge = divide_geo_node.createNode('object_merge', 'merge_alembic')
    obj_merge.parm('objpath1').set(alembic_input)
    obj_merge.moveToGoodPosition()
    return obj_merge


def main(alembic_path):
    subnet = create_main_subnet()
    divide_node = create_divide_into_parts_geo_node(subnet)
    divide_into_parts(divide_node, alembic_path)
