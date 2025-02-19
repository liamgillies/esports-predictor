// Roster.js
import React from 'react';
import { Box, Heading, Text } from '@chakra-ui/react';

function Roster({ roster }) {
    console.log(roster);

  return (
    <Box width="400px">
      <Heading as="h3" size="lg" mb={4}>
        Roster
      </Heading>
      <Box>
        {roster.length > 0 ? (
          roster.map(player => (
            <Box key={player} p={2} borderBottom="1px" borderColor="gray.200">
              <Text fontSize="lg">{player[1]}: {player[0]}</Text>
              {/* Display other member details here if necessary */}
            </Box>
          ))
        ) : (
          <Text>No roster available</Text>
        )}
      </Box>
    </Box>
  );
}

export default Roster;
