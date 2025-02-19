import * as React from 'react'

// 1. import `ChakraProvider` component
import { ChakraProvider, Box } from '@chakra-ui/react'
import Tournaments from './components/Tournaments/Tournaments';



function App() {
  // 2. Wrap ChakraProvider at the root of your app
  return (
    <ChakraProvider>
      <Box bg="gray.100" minHeight="100vh">
        <Tournaments />
      </Box>
    </ChakraProvider>
  )
}
export default App;