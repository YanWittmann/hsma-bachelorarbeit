-- nodes
CREATE TABLE IF NOT EXISTS nodes
(
    uid      INTEGER PRIMARY KEY AUTOINCREMENT,
    id       TEXT NOT NULL,
    nodeType TEXT NOT NULL,
    nodeData TEXT,
    UNIQUE (id, nodeType)
);
CREATE INDEX IF NOT EXISTS idx_nodes_id ON nodes (id);

-- edges
CREATE TABLE IF NOT EXISTS edges
(
    uid              INTEGER PRIMARY KEY AUTOINCREMENT,
    sourceUid        INTEGER NOT NULL,
    targetUid        INTEGER NOT NULL,
    direction        TEXT    NOT NULL,
    relationshipType TEXT    NOT NULL,
    edgeData         TEXT,

    FOREIGN KEY (sourceUid) REFERENCES nodes (uid),
    FOREIGN KEY (targetUid) REFERENCES nodes (uid),
    UNIQUE (sourceUid, targetUid, relationshipType)
);

CREATE INDEX IF NOT EXISTS idx_edges_source ON edges (sourceUid);
CREATE INDEX IF NOT EXISTS idx_edges_target ON edges (targetUid);
