# Llama 3 / Ollama wrapper

from langchain_ollama import OllamaLLM

# Create a global LLM client (local)
llm = OllamaLLM(model="llama3:8b")

def ask_llm(prompt: str) -> str:
    """
    General-purpose LLM response for theory/stat questions.
    """
    system_prompt = """
    You are StatMate, an expert statistics tutor.
    Answer the question clearly and concisely.
    Provide formulas or Python examples if useful.
    Do not hallucinate; if unknown, say 'I don't know'.
    """
    query = f"{system_prompt}\n\nQ: {prompt}\nA:"
    result = llm.invoke(query).strip()
    return result

def decide_test(prompt: str) -> str:
    """
    Given a user's question about data, ask the LLM which statistical test applies.
    Returns a keyword (like 'paired_ttest', 'anova', 'correlation').
    """
    system_prompt = """
    You are an expert statistician.
    Given a natural-language question about data, 
    respond ONLY with one of the following test names:
    [independent_ttest, paired_ttest, anova, correlation, regression, chi_square, describe]
    Example:
    Q: Compare before and after scores -> paired_ttest
    """
    query = f"{system_prompt}\n\nQ: {prompt}\nA:"
    result = llm.invoke(query).strip().lower()
    return result
