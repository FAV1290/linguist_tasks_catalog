from enum import Enum


class TaskPricingType(Enum):
    runtime_only = 'R'
    events_only = 'E'
    custom_only = 'C'
    runtime_and_events = 'RE'

    @property
    def show_label(self) -> str:
        types_to_labels_map = {
            'R': 'Runtimes only pricing',
            'E': 'Events only pricing',
            'C': 'Custom pricing',
            'RE': 'Runtimes and events pricing',
        }
        return types_to_labels_map[self.value]


class TaskStatus(Enum):
    assigned = 'assigned'
    in_progress = 'in progress'
    completed = 'completed'
