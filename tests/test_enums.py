from webapp.enums import TaskPricingType


def test_show_label() -> None:
    types_to_labels_map = {
        'R': 'Runtimes only pricing',
        'E': 'Events only pricing',
        'C': 'Custom pricing',
        'RE': 'Runtimes and events pricing',
    }
    for index, value in types_to_labels_map.items():
        test_type = TaskPricingType(index)
        assert test_type.show_label() == value
