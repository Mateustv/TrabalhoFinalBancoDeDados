import GlobalStyle from "./styles/global.js";
import styled from "styled-components";
import Form from "./components/Form.js";
import { useEffect, useState } from "react";
import { toast, ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import Grid from "./components/Grid.js";
import axios from "axios";

const Container = styled.div`
  width: 100%;
  max-width: 2200px;
  margin-top: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
`;

const Title = styled.h2``;

function App() {
  const [ocorrencias, setOcorrencias] = useState([]);
  const [onEdit, setOnEdit] = useState(null);

  const getOcorrencias = async () => {
    try {
      const res = await axios.get("http://localhost:8800");
      setOcorrencias(res.data.sort((a, b) => (a.nome > b.nome ? 1 : -1)));
    } catch (error) {
      toast.error(error);
    }
  };

  useEffect(() => {
    getOcorrencias();
  }, [setOcorrencias]);

  return (
    <>
      <Container>
        <Title>Ocorrências</Title>
        <Form />
        <Grid ocorrencias={ocorrencias} />
      </Container>
      <ToastContainer autoClose={3000} position={toast.POSITION.BOTTOM_LEFT} />
      <GlobalStyle />
    </>
  );
}

export default App;
