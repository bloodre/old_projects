import System.IO
import Control.Monad
import Data.List

main :: IO ()
main = do
    hSetBuffering stdout NoBuffering -- DO NOT REMOVE
    
    -- Auto-generated code below aims at helping you parse
    -- the standard input according to the problem statement.
    
    input_line <- getLine
    let input = words input_line
    let n = read (input!!0) :: Int -- the total number of nodes in the level, including the gateways
    let l = read (input!!1) :: Int -- the number of links
    let e = read (input!!2) :: Int -- the number of exit gateways
    
    graph <- replicateM l $ do
        input_line <- getLine
        let input = words input_line
        let n1 = read (input!!0) :: Int -- N1 and N2 defines a link between these nodes
        let n2 = read (input!!1) :: Int
        return ((n1,n2))
    let subGraph = subList 2 graph
    
    gates <- replicateM e $ do
        input_line <- getLine
        let ei = read input_line :: Int -- the index of a gateway node
        return (ei)
    loop subGraph gates n l 

--loop :: (Eq a) => [[(a,a)]] -> [a] -> a -> a -> IO () -- marre des problèmes de type
loop subGraph gates n l = do
    input_line <- getLine
    let si = read input_line :: Int -- The index of the node on which the Skynet agent is positioned this turn
    
    let pathToCut = shortestList . map (shortestList) . filter (/= []) . map ($ subGraph) . map (limitedPaths si) $ gates
    let linkToCut = snd $ head $ closeNodes si pathToCut
    
    
    -- Example: 0 1 are the indices of the nodes you wish to sever the link between
    
    putStrLn (show(fst linkToCut) ++ " " ++ show(snd linkToCut) )
    
    loop subGraph gates n l 
  
  
-------------------------------------------------- useful functions    
subList :: (Eq a) => Int -> [a] -> [[a]] -- give all the sublist of size <= n of a list 
subList 0 l = [[]]
subList n [] = [[]]
subList n (x:xs) = (map (x:) $ subList (n-1) xs) ++ (subList n xs)


shortestList :: (Eq a) => [[a]] -> [a]
shortestList [l] = l 
shortestList (l :ls) 
    | (length l) <= length (shortestList ls) = l
    | otherwise     = shortestList ls
            
	


closeNodes :: (Eq a) => a -> [(a,a)] -> [(a,(a,a))] -- return a list of close nodes inside a path of a given node including the link with it
closeNodes node graph =
    let isInLink node link 
                | (fst link == node) || (snd link == node) = True
                | otherwise = False
        ;otherNode node link 
                | fst link == node = snd link
                | snd link == node = fst link
    in [(otherNode node link, link)| link <- graph, isInLink node link] 


isPath :: (Eq a) => a -> a -> [(a,a)] -> Bool  -- take two nodes and say if the links in the list makes a path between the two nodes
isPath a b [] 
        | a == b = True
        | otherwise = False
isPath a b path = elem True $ [isPath cnode b $ delete link path| (cnode,link) <- closeNodes a path]
 
			
limitedPaths :: (Eq a) => a -> a -> [[(a,a)]] -> [[(a,a)]] -- return the pahts between two nodes of a lenght below a given number
limitedPaths n1 n2 subGraph = filter (isPath n1 n2) subGraph -- should calculate sublist once

