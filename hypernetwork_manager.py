import logging
from typing import Dict, List, Set
from datetime import datetime

class Hyperedge:
    def __init__(self, source: str, target: str, weight: float):
        self.source = source
        self.target = target
        self.weight = weight
        self.last_updated = datetime.now()

class HypernetworkManager:
    def __init__(self):
        self.hyperedges = {}  # type: Dict[str, List[Hyperedge]]
        self.domain_connections = {}  # type: Dict[str, Set[str]]

    def add_hyperedge(self, source: str, target: str, weight: float) -> None:
        """Add a hyperedge between domains."""
        key = f"{source}_{target}"
        if key not in self.hyperedges:
            self.hyperedges[key] = []
            self.domain_connections[source].add(target)
            self.domain_connections[target].add(source)
        self.hyperedges[key].append(Hyperedge(source, target, weight))
        logging.info(f"Added hyperedge from {source} to {target}")

    def update_hyperedge(self, source: str, target: str, new_weight: float) -> None:
        """Update the weight of an existing hyperedge."""
        key = f"{source}_{target}"
        if key in self.hyperedges:
            for edge in self.hyperedges[key]:
                if edge.source == source and edge.target == target:
                    edge.weight = new_weight
                    edge.last_updated = datetime.now()
                    logging.info(f"Updated hyperedge weight from {source} to {target}")
                    return
        raise ValueError("Hyperedge not found")

    def remove_hyperedge(self, source: str, target: str) -> None:
        """Remove a hyperedge between domains."""
        key = f"{source}_{target}"
        if key in self.hyperedges:
            del self.hyperedges[key]
            logging.info(f"Removed hyperedge from {source} to {target}")
        else:
            raise ValueError("Hyperedge not found")

    def get_connection_status(self, source: str, target: str) -> bool:
        """Check if a connection exists between domains."""
        key = f"{source}_{target}"
        return key in self.hyperedges

    def handle_edge_failure(self, source: str, target: str) -> None:
        """Handle failure of a hyperedge by rerouting connections."""
        key = f"{source}_{target}"
        if key in self.hyperedges:
            del self.hyperedges[key]
            # Reroute through alternative paths
            alternatives = self.find_alternative_paths(source, target)
            if alternatives:
                logging.info(f"Found alternative paths: {alternatives}")
                for alt in alternatives:
                    self.add_hyperedge(alt[0], alt[1], 0.5)
            else:
                logging.warning("No alternative paths found")
        else:
            logging.error("Hyperedge not found")

    def find_alternative_paths(self, source: str, target: str) -> List[List[str]]:
        """Find alternative paths between domains."""
        # Simplified example; real implementation would use a graph traversal algorithm
        return [[source, 'intermediate', target]]

    def log_activity(self, message: str) -> None:
        """Log system activity with timestamp."""
        logging.info(f"{datetime.now()}: {message}")