import * as React from 'react';
import { Box, Heading, Text, VStack, Alert } from '@chakra-ui/react';
import { useState } from 'react';

function Teams({ teams, setRoster }) {
  // Define an array of colors for variety
  const colors = ['red.200', 'blue.200', 'green.200', 'yellow.200', 'purple.200', 'pink.200', 'teal.200', 'orange.200'];

  return (
    <Box width="400px">
      <Heading as="h2" size="xl" mb={4}>
        Teams
      </Heading>
      {teams.length === 0 ? (
        <Text>No teams found</Text>
      ) : (
        <VStack spacing={2}>
          {teams.map((team, index) => (
            <Box
              key={index}
              p={4}
              borderWidth="1px"
              borderRadius="md"
              width="100%"
              bg={colors[index % colors.length]} // Assign different colors cyclically
              _hover={{
                bg: 'gray.300', // Change background on hover
                cursor: 'pointer',
                transform: 'scale(1.05)', // Slight scale-up effect
                transition: 'all 0.2s',
              }}
              onClick={() => {
                const players = team.rosterLinks?.split(";;");
                const roles = team.roles?.split(";;");
                if (!players) {
                    return;
                }
                setRoster((players.map((player, i) => [player, roles[i]])).filter(person => person[1] !== 'Coach'))
            }}
            >
              <Text fontSize="lg" fontWeight="bold">{team.team}</Text>
            </Box>
          ))}
        </VStack>
      )}
    </Box>
  );
}

export default Teams;