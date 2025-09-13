import pixeltable as pxt
from pixeltable.iterators import DocumentSplitter

docs = pxt.get_table('pixeltable_db.docs')

chunks_v = pxt.create_view(
    'pixeltable_db.docs_chunks',
    docs,
    iterator=DocumentSplitter.create(
        document=docs.content,
        separators='paragraph, token_limit',
        limit=350,
        metadata='page,title, heading,sourceline,bounding_box'
    )
)