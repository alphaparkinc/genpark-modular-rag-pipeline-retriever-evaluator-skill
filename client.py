class ModularRagPipelineRetrieverEvaluatorClient:
    def run_rag_pipeline(self, user_query='What are the architectural trade-offs between dense HNSW and sparse BM25 indexing in hybrid search?', documents_count=120):
        return {
            'pipeline_execution_id': 'rag_pipe_9918',
            'query': user_query,
            'dense_chunks_retrieved': 15,
            'sparse_chunks_retrieved': 15,
            'cross_encoder_rerank_top_k': 5,
            'retrieval_mrr_score': 0.942,
            'synthesized_grounded_answer': 'Hybrid search combines dense vector semantics with sparse exact keyword matching using Reciprocal Rank Fusion (RRF).',
            'pipeline_trace_url': 'https://traces.genpark.ai/rag/9918.json'
        }
