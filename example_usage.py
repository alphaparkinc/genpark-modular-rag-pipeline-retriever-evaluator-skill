from client import ModularRagPipelineRetrieverEvaluatorClient

def main():
    client = ModularRagPipelineRetrieverEvaluatorClient()
    res = client.run_rag_pipeline('Explain speculative decoding verification steps in vLLM')
    print('RAG Pipeline Run: ' + res['pipeline_execution_id'] + ' | Query: ' + res['query'][:40] + '...')
    print('Retrieved: ' + str(res['dense_chunks_retrieved'] + res['sparse_chunks_retrieved']) + ' chunks -> Top ' + str(res['cross_encoder_rerank_top_k']) + ' Reranked (MRR: ' + str(res['retrieval_mrr_score']) + ')')
    print('Answer: ' + res['synthesized_grounded_answer'])
    print('Trace URL: ' + res['pipeline_trace_url'])

if __name__ == '__main__':
    main()
