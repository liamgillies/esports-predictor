import * as React from 'react';
import { ChakraProvider, Box, Heading, Text, Spinner, Input, Flex, Spacer } from '@chakra-ui/react';
import { TournamentCards } from './TournamentCards';
import Teams from '../Teams/Teams';
import Roster from '../Teams/Roster';
import { useState, useEffect } from 'react';

function Tournaments() {
  const [tournaments, setTournaments] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [searchTerm, setSearchTerm] = useState('');
  const [teams, setTeams] = useState([]);
  const [roster, setRoster] = useState([]);

  // Fetch tournament data from the backend API
  useEffect(() => {
    fetch('http://localhost:8000/currentTournaments')
      .then((response) => response.json())
      .then((data) => {
        setTournaments(data);
        console.log(data);
        setLoading(false);
      })
      .catch((error) => {
        setError(error);
        setLoading(false);
      });
  }, []);

  // Filter tournaments based on search term
  const filteredTournaments = tournaments.filter((tournament) =>
    tournament.name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <ChakraProvider>
      <Flex direction="row" p={5} align="flex-start">
        {/* Left Side: Tournaments & Teams Section */}
        <Flex direction="row" width="800px" gap={5}>
          {/* Tournaments List */}
          <Box width="400px">
            <Flex align="center" justify="space-between" mb={4}>
              <Heading as="h2" size="xl">
                Tournaments
              </Heading>
              <Input
                placeholder="Search"
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                width="150px"
                height="40px"
                borderRadius="md"
                boxShadow="md"
                border="2px solid"
                borderColor="white.500"
              />
            </Flex>

            {loading ? (
              <Spinner size="xl" />
            ) : error ? (
              <Text color="red.500" fontSize="xl">
                Something went wrong: {error.message}
              </Text>
            ) : filteredTournaments.length === 0 ? (
              <Text>No tournaments found</Text>
            ) : (
              <TournamentCards filteredTournaments={filteredTournaments} setTeams={setTeams} />
            )}
          </Box>

          {/* Teams List */}
          <Teams teams={teams} setRoster={setRoster} />

          {/* Roster List */}
          <Roster roster={roster}/>
        </Flex>

        {/* Spacer to separate Tournament Details */}
        <Spacer />

        {/* Right Side: Tournament Details */}
        <Box flex="1" p={5}>
          <Heading as="h2" size="xl" mb={4}>
            Tournament Details
          </Heading>
          <Text>Select a tournament to view details</Text>
        </Box>
      </Flex>
    </ChakraProvider>
  );
}

export default Tournaments;
