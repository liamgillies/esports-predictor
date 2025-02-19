import * as React from 'react';
import { VStack, Card, CardBody, Stack, Text } from '@chakra-ui/react';

// Handle card click and update the team name
const handleCardClick = (tournamentName, setTeams) => {
  console.log('Fetching rosters for tournament:', tournamentName);
  
  fetch(`http://localhost:8000/tournaments/${tournamentName}/rosters`)
    .then((response) => {
      if (!response.ok) {
        throw new Error(`Failed to fetch rosters for ${tournamentName}`);
      }
      return response.json();
    })
    .then((data) => {
      if (data) {
        console.log(data);
        setTeams(data); // Update the teamName state
      } else {
        console.error('Team name not found in the response:', data);
      }
    })
    .catch((error) => {
      console.error('Error fetching data:', error); // Log the error
    });
};

export function TournamentCards({ filteredTournaments, setTeams }) {
  return (
    <VStack spacing={2}>
      {filteredTournaments.slice(0, 15).map((tournament, index) => (
        <Card
          key={index}
          width="100%"
          boxShadow="lg"
          p={0}
          _hover={{ boxShadow: 'xl', transform: 'scale(1.05)', cursor: 'pointer' }}
          transition="all 0.3s"
          onClick={() => handleCardClick(tournament.name, setTeams)} // Pass setTeamName as a prop
        >
          <CardBody>
            <Stack direction="row" align="center" spacing={-1}>
              <Text fontSize="lg" fontWeight="bold" noOfLines={0} isTruncated>
                {tournament.name},{tournament.dateStart}
              </Text>
            </Stack>
          </CardBody>
        </Card>
      ))}
    </VStack>
  );
}
