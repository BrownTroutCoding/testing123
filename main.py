"""
Manages a collection of documents.
Attributes:
    documents (list of str): A list that stores the documents.
"""
class DocumentManager:
    """Initializes the DocumentManager with an empty list of documents"""
    def __init__(self):
        self.documents = []
    
    """
    Adds a single document to the documents list.

    Args:
        document (str):  Document that is added to the list.

    Raises: 
        TypeError: If the provided document is not a string.

    Examples:
        >>> manager = Documentmanager()
        >>> manager.add_document("Doc 1")
        >>> print(manager.documents)
        ['Doc 1']
    """
    def add_document(self, document):

        if not isinstance(document, str):
            raise TypeError("Document must be a string.")
        self.documents.append(document)

    """
    Adds documents to the documents list.

    Args:
        documents (list of str): A list of documents to be added.
    
    Raises:
        TypeError: If the provided documents are not in a list

    Examples:
        >>> manager = Documentmanager()
        >>> manager.add_document([]"Doc 2", "Doc 3"])
        >>> print(manager.documents)
        ['Doc 1', 'Doc 2', 'Doc 3']
    """
    def add_documents(self, documents):
        if not isinstance(documents, list):
            raise TypeError("Documents must be provided as a list.")
        for doc in documents:
            if not isinstance(doc, str):
                raise TypeError("Each document must be a string.")
        self.documents.extend(documents)


    """
    Removes a document from the documents list.

    Args:
        document (str): The document to be removed from the list

    Raises:
        ValueError: If the document is not found in the list
    
    Examples:
        >>> manager = Documentmanager()
        >>> manager.add_document([]"Doc 2", "Doc 2"])
        >>> manager.remove_document("Doc 1")
        >>> print(manager.documents)
        ['Doc 2']
    """
    def remove_document(self, document):
        if document not in self.documents:
            raise ValueError("Document not found in the list.")
        self.documents.remove(document)


    """
    Clears all documents from the list.

    Examples:
        >>> manager = Documentmanager()
        >>> manager.add_document([]"Doc 2", "Doc 2"])
        >>> manager.clear_documents()
        >>> print(manager.documents)
        []

    """
    def clear_documents(self):
        self.documents.clear()

manager = DocumentManager()
manager.add_document("Document 1")
manager.add_documents(["Document 2", "Document 3"])
print(manager.documents)
manager.remove_document("Document 2")
print(manager.documents)
manager.clear_documents()
print(manager.documents)