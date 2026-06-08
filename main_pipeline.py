from utils.pdf_loader import extract_text_from_pdf
from utils.text_cleaner import clean_text
from utils.langchain_chunker import split_text

from modules.summarizer import generate_summary_from_chunks
from modules.extractor import extract_entities_from_chunks
from modules.table_generator import generate_table
from modules.indexer import index_chunks



def run_pipeline(pdf_path):

    print("📄 Loading PDF...")
    raw_text = extract_text_from_pdf(pdf_path)

    print("🧹 Cleaning text...")
    cleaned_text = clean_text(raw_text)

    print("✂️ Creating chunks...")
    chunks = split_text(cleaned_text)
    chunks = chunks[:2]
    index_chunks(chunks)

    print(f"Created {len(chunks)} chunks")

    print("\n📝 Generating Summary...")
    summary = "SKIPPED FOR TESTING"

    print("\n🔍 Extracting Entities...")
    entities = extract_entities_from_chunks(chunks)

    print("\n📊 Generating Table...")
    table = generate_table(entities)

    return {
        "summary": summary,
        "entities": entities,
        "table": table
    }


if __name__ == "__main__":

    result = run_pipeline(
        "data/test1.pdf"
    )

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(result["summary"])

    print("\n" + "=" * 60)
    print("ENTITIES")
    print("=" * 60)
    print(result["entities"])

    print("\n" + "=" * 60)
    print("TABLE")
    print("=" * 60)
    print(result["table"])