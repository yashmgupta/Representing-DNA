import streamlit as st
import numpy as np

# Function for One-hot encoding
def one_hot_encode(dna):
    nucleotides = 'ATGC'
    encoding = {nucleotide: i for i, nucleotide in enumerate(nucleotides)}
    one_hot_encoded = np.zeros((len(dna), len(nucleotides)))
    for i, nucleotide in enumerate(dna):
        if nucleotide in encoding:
            one_hot_encoded[i, encoding[nucleotide]] = 1
    return one_hot_encoded

# Corrected Function for Binary encoding
def binary_encode(dna):
    binary_map = {'A': [0, 0], 'T': [0, 1], 'G': [1, 0], 'C': [1, 1]}  # Correct binary representation
    return np.array([binary_map[nucleotide] for nucleotide in dna if nucleotide in binary_map])

# Function for Integer encoding
def integer_encode(dna):
    int_map = {'A': 0, 'T': 1, 'G': 2, 'C': 3}
    return [int_map[nucleotide] for nucleotide in dna if nucleotide in int_map]

# Streamlit application main function
def main():
    st.title('DNA Sequence Encoding and Machine Learning Explanation')

    user_input = st.text_input('Enter a DNA sequence:', 'ATGCCTAGTTACG')

    page = st.sidebar.selectbox("Choose a Page", ["Encoding Methods", "Machine Learning Explanation", "Encoding Code Explanation"])

    if page == "Encoding Methods":
        encoding_method = st.sidebar.selectbox("Choose an Encoding Method", ["One-hot Encoding", "Binary Encoding", "Integer Encoding"])

        if encoding_method == "One-hot Encoding":
            st.header("One-hot Encoding")
            st.write("Each nucleotide is represented as a unique vector.")
            if st.button('Encode One-hot'):
                result = one_hot_encode(user_input)
                st.text_area("One-hot encoded sequence:", value=str(result), height=150)

        elif encoding_method == "Binary Encoding":
            st.header("Binary Encoding")
            st.write("Each nucleotide is assigned a unique binary vector.")
            if st.button('Encode Binary'):
                result = binary_encode(user_input)
                st.text_area("Binary encoded sequence:", value=str(result), height=150)

        elif encoding_method == "Integer Encoding":
            st.header("Integer Encoding")
            st.write("Each nucleotide is represented by a unique integer.")
            if st.button('Encode Integer'):
                result = integer_encode(user_input)
                st.text_area("Integer encoded sequence:", value=str(result), height=100)

    elif page == "Machine Learning Explanation":
        st.header("Machine Learning Demo on DNA Encoding Methods")
        st.write("""
        This section provides a theoretical explanation of how encoded DNA sequences can be used to train machine learning models.
        We discuss the process step by step without actual training to understand the underlying concepts.
        """)

        st.write("### Step 1: Encoding DNA Sequences")
        st.write("First, we convert DNA sequences into numerical data via encoding methods such as One-hot, Binary, or Integer.")

        st.write("### Step 2: Preparing the Dataset")
        st.write("The numerical data is then split into training and testing sets.")

        st.write("### Step 3: Model Selection and Training")
        st.write("A machine learning model (like Logistic Regression) is selected and trained on the training set.")

        st.write("### Step 4: Evaluation")
        st.write("Finally, the model's performance is evaluated on the testing set using metrics such as accuracy.")

    elif page == "Encoding Code Explanation":
        st.header("DNA Sequence Encoding Code Explanation")
        st.write("""
        ### One-hot Encoding Function
        Converts each nucleotide in a DNA sequence into a one-hot encoded vector. This representation uses four positions to represent each nucleotide, with one position filled with 1 and the rest with 0.
        ```python
        def one_hot_encode(dna):
            nucleotides = 'ATGC'
            encoding = {nucleotide: i for i, nucleotide in enumerate(nucleotides)}
            one_hot_encoded = np.zeros((len(dna), len(nucleotides)))
            for i, nucleotide in enumerate(dna):
                if nucleotide in encoding:
                    one_hot_encoded[i, encoding[nucleotide]] = 1
            return one_hot_encoded
        ```
        ### Binary Encoding Function
        Assigns each nucleotide in a DNA sequence a unique binary vector.
        ```python
        def binary_encode(dna):
            binary_map = {'A': [0, 0], 'T': [0, 1], 'G': [1, 0], 'C': [1, 1]}
            return np.array([binary_map[nucleotide] for nucleotide in dna if nucleotide in binary_map])
        ```
        ### Integer Encoding Function
        Maps each nucleotide in a DNA sequence to a unique integer.
        ```python
        def integer_encode(dna):
            int_map = {'A': 0, 'T': 1, 'G': 2, 'C': 3}
            return [int_map[nucleotide] for nucleotide in dna if nucleotide in int_map]
        ```
        """)

if __name__ == "__main__":
    main()
