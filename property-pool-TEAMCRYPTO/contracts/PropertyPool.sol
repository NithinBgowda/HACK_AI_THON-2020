// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.8.0;
pragma experimental ABIEncoderV2;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/access/AccessControl.sol";

// import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC721/ERC721.sol";
// import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/access/AccessControl.sol";
// import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/access/Ownable.sol";

contract PropertyPool is ERC721, Ownable, AccessControl {
    bytes32 public constant MINTER_ROLE = keccak256("MINTER_ROLE");
    bytes32 public constant MINTER_ADMIN_ROLE = keccak256("MINTER_ADMIN_ROLE");

    struct Property {
        string propertyId;
        string propertyAddress;
        uint256 propertyLength;
        uint256 propertyWidth;
    }

    Property[] private properties;

    constructor() public ERC721("PropertyPool", "PPL") {
        _setRoleAdmin(MINTER_ROLE, MINTER_ADMIN_ROLE);
        _setupRole(MINTER_ADMIN_ROLE, msg.sender);

        Property memory _property = Property("000", "India", 0, 0);
        properties.push(_property);
        uint256 _tokenId = properties.length - 1;
        _mint(msg.sender, _tokenId);
    }

    event PropertyMinted(address _owner, uint256 _tokenId);
    event PropertyTransfered(address _from, address _to, uint256 _tokenId);

    function addMinters(address minter) public onlyOwner {
        grantRole(MINTER_ROLE, minter);
    }

    function removeMinters(address minter) public onlyOwner {
        revokeRole(MINTER_ROLE, minter);
    }

    function mintProperty(
        string memory _propertyId,
        string memory _propertyAddress,
        uint256 _propertyLength,
        uint256 _propertyWidth,
        address _owner
    ) public {
        require(hasRole(MINTER_ROLE, msg.sender));

        Property memory _property = Property(
            _propertyId,
            _propertyAddress,
            _propertyLength,
            _propertyWidth
        );
        properties.push(_property);
        uint256 _tokenId = properties.length - 1;

        _mint(msg.sender, _tokenId);
        transferProperty(msg.sender, _owner, _tokenId);
        emit PropertyMinted(_owner, _tokenId);
    }

    function transferProperty(
        address _from,
        address _to,
        uint256 _tokenId
    ) public {
        transferFrom(_from, _to, _tokenId);
        emit PropertyTransfered(_from, _to, _tokenId);
    }

    function getPropertyFromId(uint256 id)
        public
        view
        returns (Property memory)
    {
        return (properties[id]);
    }

    function getAllProperties() public view returns (Property[] memory) {
        return properties;
    }
}
